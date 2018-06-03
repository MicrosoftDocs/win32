---
title: MSFT\_SoftError\_EmptyCache class
description: Represents an empty-cache error.
ms.assetid: 9B5449D1-C89A-4087-B2C0-FA66BD8E6D6E
keywords:
- MSFT_SoftError_EmptyCache class Windows Storage Management API
- MSFT_SoftError_EmptyCache class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_SoftError_EmptyCache
- MSFT_SoftError_EmptyCache.MessageID
- MSFT_SoftError_EmptyCache.Message
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SoftError\_EmptyCache class

Represents an empty-cache error.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError_EmptyCache : MSFT_SoftError
{
  String MessageID;
  String Message;
};
```

## Members

The **MSFT\_SoftError\_EmptyCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError\_EmptyCache** class has these properties.

<dl> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message displayed to the user. The value of this property is "%1: The storage management provider's cache is empty.%2".

"%1" should be replaced with the corresponding storage provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" can be replaced with extra error information.

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message identifier. The value of this property is "40003". This is the specific error code for 'Cache out of date'.

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

 

 





