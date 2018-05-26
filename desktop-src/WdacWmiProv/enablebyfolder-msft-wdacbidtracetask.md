---
title: EnableByFolder method of the MSFT\_WdacBidTraceTask class
description: Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 245fedb8-02d0-4a3b-8990-05bb9b840b37
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableByFolder method
- EnableByFolder method, MSFT_WdacBidTraceTask class
- MSFT_WdacBidTraceTask class, EnableByFolder method
topic_type:
- apiref
api_name:
- MSFT_WdacBidTraceTask.EnableByFolder
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableByFolder method of the MSFT\_WdacBidTraceTask class

Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.

## Syntax


```mof
uint32 EnableByFolder(
  [in]  boolean           PassThru,
  [in]  string            Platform,
  [in]  string            Folder,
  [out] MSFT_WdacBidTrace cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*Platform* \[in\]
</dt> <dd>

The platform architecture of the WDAC BidTrace setting. Possible values are '32-bit', '64-bit' or 'All'. The default is '32-bit' on a 32-bit process and '64-bit' on a 64-bit process. This is the platform architecture on the remote machine if this command is executed on a remote CIM session.

</dd> <dt>

*Folder* \[in\]
</dt> <dd>

Enable BidTrace for all applications under this folder.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The output is an array of CIM objects of type [**MSFT\_WdacBidTrace**](msft-wdacbidtrace.md), each of which represents a WDAC BidTrace setting.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WdacBidTraceTask**](msft-wdacbidtracetask.md)
</dt> <dt>

[**MSFT\_WdacBidTrace**](msft-wdacbidtrace.md)
</dt> </dl>

 

 





