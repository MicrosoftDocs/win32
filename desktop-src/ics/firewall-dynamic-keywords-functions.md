---
title: Firewall dynamic keywords functions
description: Firewall dynamic keywords contains the following functions.
keywords:
- Firewall dynamic keywords, functions
ms.topic: article
ms.date: 05/13/2021
---

# Firewall dynamic keywords functions

Firewall dynamic keywords contains the following functions.

## In this section

| Topic | Description |
|-|-|
| [**FwpmDynamicKeywordSubscribe0**](/windows/win32/api/fwpmu/nf-fwpmu-fwpmdynamickeywordsubscribe0) | Requests the delivery of notifications regarding changes to particular dynamic keyword address ([FW_DYNAMIC_KEYWORD_ADDRESS0](/windows/win32/api/netfw/ns-netfw-fw_dynamic_keyword_address0)) objects. |
| [**FwpmDynamicKeywordUnsubscribe0**](/windows/win32/api/fwpmu/nf-fwpmu-fwpmdynamickeywordsubscribe0) | Cancels the delivery of notifications regarding changes to particular dynamic keyword address ([FW_DYNAMIC_KEYWORD_ADDRESS0](/windows/win32/api/netfw/ns-netfw-fw_dynamic_keyword_address0)) objects. |
| [**PFN_FWADDDYNAMICKEYWORDADDRESS0**](/windows/win32/api/netfw/nc-netfw-pfn_fwadddynamickeywordaddress0) | Function pointer type of the entry point in the service that you call to add the specified dynamic keyword address. |
| [**PFN_FWDELETEDYNAMICKEYWORDADDRESS0**](/windows/win32/api/netfw/nc-netfw-pfn_fwdeletedynamickeywordaddress0) | Function pointer type of the entry point in the service that you call to delete the dynamic keyword address with the specified ID. |
| [**PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0**](/windows/win32/api/netfw/nc-netfw-pfn_fwenumdynamickeywordaddressbyid0) | Function pointer type of the entry point in the service that you call to enumerate the specific dynamic keyword addresses by ID. |
| [**PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0**](/windows/win32/api/netfw/nc-netfw-pfn_fwenumdynamickeywordaddressesbytype0) | Function pointer type of the entry point in the service that you call to enumerate dynamic keyword addresses by type. You can request a particular subset of objects based on the enumeration flags passed in. |
| [**PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0**](/windows/win32/api/netfw/nc-netfw-pfn_fwfreedynamickeywordaddressdata0) | Function pointer type of the entry point in the service that you call to free dynamic keyword address data structs allocated by the service. |
| [**PFN_FWUPDATEDYNAMICKEYWORDADDRESS0**](/windows/win32/api/netfw/nc-netfw-pfn_fwupdatedynamickeywordaddress0) | Function pointer type of the entry point in the service that you call to update the dynamic keyword address with the input ID. |

## Related topics

* [Firewall dynamic keywords reference](firewall-dynamic-keywords-reference.md)
