---
title: MSFT\_SoftError class
description: Represents a soft error.
ms.assetid: 95810BD7-A582-4B4A-A878-35CDDD949599
keywords:
- MSFT_SoftError class Windows Storage Management API
- MSFT_SoftError class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_SoftError
- MSFT_SoftError.ErrorType
- MSFT_SoftError.OwningEntity
- MSFT_SoftError.MessageID
- MSFT_SoftError.Message
- MSFT_SoftError.PerceivedSeverity
- MSFT_SoftError.ErrorSource
- MSFT_SoftError.ErrorSourceFormat
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

# MSFT\_SoftError class

Represents a soft error.

Soft errors can be returned by intrinsic methods (such as **EnumerateInstances** and **GetInstance**) to help distinguish between a query with no results (no error) and a query that fails for a specific reason.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_SoftError : CIM_Error
{
  UInt16 ErrorType;
  String OwningEntity;
  String MessageID;
  String Message;
  UInt16 PerceivedSeverity;
  String ErrorSource;
  UInt16 ErrorSourceFormat;
};
```

## Members

The **MSFT\_SoftError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SoftError** class has these properties.

<dl> <dt>

**ErrorSource**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The CIM Object Path to the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md) object.

</dd> <dt>

**ErrorSourceFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** ( "CIMObjectPath" ), **ValueMap** ("2")
</dt> </dl>

The CIM object path.

</dd> <dt>

**ErrorType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** ( "Software Error" ), **ValueMap** ("4")
</dt> </dl>

This error is of the type **Software Error**.

</dd> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message displayed to the user. The value of this property is "%1: %2".

"%1" should be replaced with the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property. "%2" should be replaced with the error message.

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message identifier.

</dd> <dt>

**OwningEntity**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Corresponds to the storage management provider's [**MSFT\_StorageProvider**](msft-storageprovider.md).**Name** property.

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** ( "Information" ), **ValueMap** ("2")
</dt> </dl>

This error is informative only.

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

[**CIM\_Error**](https://msdn.microsoft.com/library/cc150671)
</dt> </dl>

 

 





