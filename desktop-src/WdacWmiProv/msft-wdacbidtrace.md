---
title: MSFT\_WdacBidTrace class
description: WDAC BidTrace Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e49b67cc-5de7-4ee0-a695-6a00d5a7e150
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WdacBidTrace class
- MSFT_WdacBidTrace class, described
topic_type:
- apiref
api_name:
- MSFT_WdacBidTrace
- MSFT_WdacBidTrace.Platform
- MSFT_WdacBidTrace.Mode
- MSFT_WdacBidTrace.PathOrFolder
- MSFT_WdacBidTrace.ProcessId
- MSFT_WdacBidTrace.IsEnabled
- MSFT_WdacBidTrace.IsDefined
- MSFT_WdacBidTrace.BidTraceAdapter
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WdacBidTrace class

WDAC BidTrace Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class MSFT_WdacBidTrace
{
  string  Platform;
  uint32  Mode;
  string  PathOrFolder;
  uint32  ProcessId;
  boolean IsEnabled;
  boolean IsDefined;
  string  BidTraceAdapter;
};
```

## Members

The **MSFT\_WdacBidTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WdacBidTrace** class has these properties.

<dl> <dt>

**BidTraceAdapter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The full path of the BidTrace adapter.

</dd> <dt>

**IsDefined**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the WDAC BidTrace setting is defined.

</dd> <dt>

**IsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the WDAC BidTrace setting is enabled.

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

One of the following: 1 (= Full path); 2 (= Folder); 3 (= All applications).

</dd> <dt>

**PathOrFolder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The full path of applications for the BidTrace configuration (when Mode == 1), or the full path of application folder for the BidTrace configuration (when Mode==2). This is ignored for Mode == 3.

</dd> <dt>

**Platform**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The platform architecture of the BidTrace setting. Either '32-bit' or '64-bit'.

</dd> <dt>

**ProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The process ID of a particular application for the BidTrace configuration. This is ignored for Mode != 1.

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

[WDAC WMI Provider Reference](wdac-wmi-provider-reference.md)
</dt> </dl>

 

 





