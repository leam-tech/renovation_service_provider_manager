# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import requests

__version__ = '0.0.1'


def invoke_mediator(api, body=None) -> requests.Response:

  k = get_mediator_creds()
  return requests.post(
      url="{}{}".format(k.mediator_url, api),
      headers={
          "Authorization": format_basic_auth_header(k.api_key, k.api_secret),
          "Accept": "application/json"
      },
      json=body
  )


def get_mediator_creds():
  d = frappe.get_site_config().get("mediator_creds")
  if not d:
    frappe.throw(
        "Please specify mediator_creds in site config of Agents Bench Manager site")

  for x in ["mediator_url", "api_key", "api_secret"]:
    if x not in d:
      frappe.throw("Please specify {} in mediator_creds".format(x))
  return frappe._dict(d)


def format_basic_auth_header(api_key, api_secret):
  from base64 import b64encode
  return "Basic {}".format(frappe.safe_decode(b64encode("{}:{}".format(
      api_key,
      api_secret
  ).encode("utf-8"))))
