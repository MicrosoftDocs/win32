---
title: MSFT\_WdacBidTraceTask class
description: Task provider for the BidTrace setting for WDAC components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5b83b1b-50f4-46e4-93b0-042f1b30d38d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WdacBidTraceTask class
- MSFT_WdacBidTraceTask class, described
topic_type:
- apiref
api_name:
- MSFT_WdacBidTraceTask
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_WdacBidTraceTask class

Task provider for the BidTrace setting for WDAC components.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WdacWmiProv"), ClassVersion("1.0"), AMENDMENT]
class MSFT_WdacBidTraceTask
{
};
```

## Members

The **MSFT\_WdacBidTraceTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_WdacBidTraceTask** class has these methods.



| Method                                                                     | Description                                                                                       |
|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**DisableByAllApp**](disablebyallapp-msft-wdacbidtracetask.md)           | Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/>  |
| [**DisableByFolder**](disablebyfolder-msft-wdacbidtracetask.md)           | Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/>  |
| [**DisableByInputObject**](disablebyinputobject-msft-wdacbidtracetask.md) | Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/>  |
| [**DisableByPath**](disablebypath-msft-wdacbidtracetask.md)               | Disables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/>  |
| [**EnableByAllApp**](enablebyallapp-msft-wdacbidtracetask.md)             | Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components. <br/>  |
| [**EnableByFolder**](enablebyfolder-msft-wdacbidtracetask.md)             | Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components. <br/>  |
| [**EnableByInputObject**](enablebyinputobject-msft-wdacbidtracetask.md)   | Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components. <br/>  |
| [**EnableByPath**](enablebypath-msft-wdacbidtracetask.md)                 | Enables Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components. <br/>  |
| [**GetByAllApp**](getbyallapp-msft-wdacbidtracetask.md)                   | Retrieves Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/> |
| [**GetByFolder**](getbyfolder-msft-wdacbidtracetask.md)                   | Retrieves Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/> |
| [**GetByPath**](getbypath-msft-wdacbidtracetask.md)                       | Retrieves Built-in Diagnostics Tracing (BidTrace) for troubleshooting WDAC components.<br/> |



 

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

[WDAC WMI Provider Reference](wdac-wmi-provider-reference.md)
</dt> </dl>

 

 





