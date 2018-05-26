---
title: DisableByInputObject method of the MSFT\_WdacBidTraceTask class
description: Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a6881c8b-7fd6-4811-a41b-6df8f45dcb75
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DisableByInputObject method
- DisableByInputObject method, MSFT_WdacBidTraceTask class
- MSFT_WdacBidTraceTask class, DisableByInputObject method
topic_type:
- apiref
api_name:
- MSFT_WdacBidTraceTask.DisableByInputObject
api_location:
- WdacWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DisableByInputObject method of the MSFT\_WdacBidTraceTask class

Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.

## Syntax


```mof
uint32 DisableByInputObject(
  [in]  boolean           PassThru,
  [in]  MSFT_WdacBidTrace InputObject[],
  [out] MSFT_WdacBidTrace cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Passes the object created by this cmdlet through the pipeline. By default, this cmdlet does not pass any objects through the pipeline.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Disable the BidTrace represented by the specified BidTrace setting objects. Enter a variable that contains the objects, or type a command or expression that gets the objects.

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

 

 





