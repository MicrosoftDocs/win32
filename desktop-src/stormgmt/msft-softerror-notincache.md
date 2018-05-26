---
title: MSFT\_SoftError\_NotInCache class
description: Represents a not-in-cache error.
ms.assetid: EF2B4036-008A-49D2-A784-4089F62BEB3F
keywords:
- MSFT_SoftError_NotInCache class Windows Storage Management API
- MSFT_SoftError_NotInCache class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_SoftError_NotInCache
- MSFT_SoftError_NotInCache.MessageID
- MSFT_SoftError_NotInCache.Message
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_SoftError\_NotInCache class

Represents a not-in-cache error.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError_NotInCache : MSFT_SoftError
{
  String MessageID;
  String Message;
};
```

## Members

The **MSFT\_SoftError\_NotInCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError\_NotInCache** class has these properties.

<dl> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message displayed to the user. The value of this property is "%1: The storage management provider's cache does not contain the requested object or object type.%2"

"%1" should be replaced with the corresponding storage provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" can be replaced with extra error information.

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message identifier. The value of this property is "40006". This is the specific error code for 'Not in Cache'.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SoftError**](msft-softerror.md)
</dt> </dl>

 

 





