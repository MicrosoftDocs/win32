---
title: IGPMStatusMessage Property Methods
description: The property methods of the IGPMStatusMessage interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8d736e30-760d-43fa-ab5d-d05dc679bfbb
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMStatusMessage Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMStatusMessage Property Methods
- IGPMStatusMessage.ExtensionName
- IGPMStatusMessage.get_ExtensionName
- IGPMStatusMessage.Message
- IGPMStatusMessage.get_Message
- IGPMStatusMessage.ObjectPath
- IGPMStatusMessage.get_ObjectPath
- IGPMStatusMessage.SettingsName
- IGPMStatusMessage.get_SettingsName
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMStatusMessage Property Methods

The property methods of the [**IGPMStatusMessage**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstatusmessage) interface get the properties described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**ExtensionName**
</dt> <dd> <dl>

Name of the extension that was being processed when the message was generated.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ExtensionName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Message**
</dt> <dd> <dl>

Message, in human-readable format.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Message(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**ObjectPath**
</dt> <dd> <dl>

Path of the object to which the message applies.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ObjectPath(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**SettingsName**
</dt> <dd> <dl>

Name of the policy setting that was being processed when the message was generated.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SettingsName(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMStatusMessage is defined as 8496C22F-F3DE-4A1F-8F58-603CAAA93D7B<br/>  |



## See also

<dl> <dt>

[**IGPMStatusMessage**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstatusmessage)
</dt> <dt>

[**IGPMStatusMsgCollection**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmstatusmsgcollection)
</dt> </dl>

 

 





