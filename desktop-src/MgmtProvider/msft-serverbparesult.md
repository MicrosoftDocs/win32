---
title: MSFT\_ServerBpaResult class
description: Class that represents the results selected by a BPA path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7cf26248-6ac5-4f97-b291-67683cad3056'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_ServerBpaResult class", "MSFT_ServerBpaResult class, described"]
topic_type:
- apiref
api_name:
- MSFT_ServerBpaResult
- MSFT_ServerBpaResult.BpaXPath
- MSFT_ServerBpaResult.Values
api_location:
- MgmtProvider.dll
api_type:
- DllExport
---

# MSFT\_ServerBpaResult class

Class that represents the results selected by a BPA path.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerBpaResult
{
  string BpaXPath;
  string Values[];
};
```

## Members

The **MSFT\_ServerBpaResult** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerBpaResult** class has these properties.

<dl> <dt>

**BpaXPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The BPA path that generated the results.

</dd> <dt>

**Values**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value selected by the BPA path.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetServerBpaResult method of MSFT\_ServerManagerTasks**](getserverbparesult-msft-servermanagertasks.md)
</dt> </dl>

 

 





