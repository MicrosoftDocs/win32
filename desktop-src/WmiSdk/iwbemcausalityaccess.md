---
description: Keeps track of child requests that are generated from a parent request.
ms.assetid: e1d98eae-6fc1-489b-aa8b-2e86bac5c65a
ms.tgt_platform: multiple
title: IWbemCausalityAccess interface (Wbemint.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWbemCausalityAccess
api_type: 
- COM
api_location: 
- Fastprox.dll
---

# IWbemCausalityAccess interface

The **IWbemCausalityAccess** interface keeps track of child requests that are generated from a parent request. You can obtain an **IWbemCausalityAccess** object by using a query interface (QI) for [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext). Each request is identified by a Globally Unique Identifier (GUID) and can have a parent request or can be a top request. A GUID is a unique 128-bit number. For example, 5b2fc63a-8af4-44cb-960c-aefdced908d6.

## Members

The **IWbemCausalityAccess** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWbemCausalityAccess** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWbemCausalityAccess** interface has these methods.



| Method                                                    | Description                                                                                                                                                             |
|:----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRequestId**](iwbemcausalityaccess-getrequestid.md) | Returns a unique GUID identifier for a request.<br/>                                                                                                              |
| [**IsChildOf**](iwbemcausalityaccess-ischildof.md)       | Determines if a request is a child of a specified parent request. A parent request can have multiple child requests, each identified by a unique GUID value.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemint.h</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Fastprox.dll</dt> </dl> |



## See also

<dl> <dt>

[COM API for WMI](com-api-for-wmi.md)
</dt> </dl>

 

