---
title: GetByFolder method of the MSFT\_WdacBidTraceTask class
description: Retrieves Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c4494490-6e1f-42a7-be4f-51ab5e618963'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByFolder method", "GetByFolder method, MSFT_WdacBidTraceTask class", "MSFT_WdacBidTraceTask class, GetByFolder method"]
topic_type:
- apiref
api_name:
- MSFT_WdacBidTraceTask.GetByFolder
api_location:
- WdacWmiProv.dll
api_type:
- COM
---

# GetByFolder method of the MSFT\_WdacBidTraceTask class

Retrieves Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.

## Syntax


```mof
uint32 GetByFolder(
  [in]  string            Platform,
  [in]  string            Folder,
  [out] MSFT_WdacBidTrace cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the WDAC BidTrace setting. Possible values are '32-bit', '64-bit' or 'All'. The default is 'All'. This is the platform architecture on the remote machine if this command is executed on a remote CIM session.

</dd> <dt>

*Folder* \[in\]
</dt> <dd>

Gets only WDAC BidTrace settings that are associated with the specified folder. You can use wildcard characters.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_WdacBidTrace**](msft-wdacbidtrace.md), each of which represents a WDAC BidTrace setting.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WdacBidTraceTask**](msft-wdacbidtracetask.md)
</dt> <dt>

[**MSFT\_WdacBidTrace**](msft-wdacbidtrace.md)
</dt> </dl>

 

 





