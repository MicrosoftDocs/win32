---
title: MSFT\_SMFabric class
description: Represents a Windows Fabric storage service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6fddfcd9-94fe-497c-8897-2be53ac1e966
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMFabric class
- MSFT_SMFabric class, described
topic_type:
- apiref
api_name:
- MSFT_SMFabric
- MSFT_SMFabric.ObjectId
- MSFT_SMFabric.ElementName
- MSFT_SMFabric.Name
- MSFT_SMFabric.NameFormat
- MSFT_SMFabric.OtherIdentifyingInfo
- MSFT_SMFabric.IdentifyingDescriptions
- MSFT_SMFabric.ManagementServer
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMFabric class

Represents a Windows Fabric storage service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMFabric
{
  String ObjectId;
  String ElementName;
  String Name;
  string NameFormat;
  String OtherIdentifyingInfo[];
  String IdentifyingDescriptions[];
  String ManagementServer;
};
```

## Members

The **MSFT\_SMFabric** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFabric** class has these properties.

<dl> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the service that is displayed to users.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains descriptions of the format used in the custom identifiers in **OtherIdentifyingInfo**. There must be a 1:1 mapping between this array and **OtherIdentifyingInfo**.

</dd> <dt>

**ManagementServer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the management server that hosts the Windows Fabric service.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The label of the service.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format or protocol for assigning the **Name** property.

The possible values are.

<dt>



 ("Other")


</dt> <dd></dd> <dt>



 ("IP")


</dt> <dd></dd> <dt>



 ("Dial")


</dt> <dd></dd> <dt>



 ("HID")


</dt> <dd></dd> <dt>



 ("NWA")


</dt> <dd></dd> <dt>



 ("HWA")


</dt> <dd></dd> <dt>



 ("X25")


</dt> <dd></dd> <dt>



 ("ISDN")


</dt> <dd></dd> <dt>



 ("IPX")


</dt> <dd></dd> <dt>



 ("DCC")


</dt> <dd></dd> <dt>



 ("ICD")


</dt> <dd></dd> <dt>



 ("E.164")


</dt> <dd></dd> <dt>



 ("SNA")


</dt> <dd></dd> <dt>



 ("OID/OSI")


</dt> <dd></dd> <dt>



 ("WWN")


</dt> <dd></dd> <dt>



 ("NAA")


</dt> <dd></dd> </dl>

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains custom identifiers for the service. If this field is set, the **OtherIdentifyingInfoDescription** property must also be set.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





