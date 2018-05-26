---
title: GetElementWithFlags method of the BcdObject class
description: Gets the specified element. This method can be used to enumerate a qualified partition.
ms.assetid: 3f162ea7-c648-48e3-98c0-c8a230704e5d
keywords:
- GetElementWithFlags method Boot Config
- GetElementWithFlags method Boot Config , BcdObject class
- BcdObject class Boot Config , GetElementWithFlags method
topic_type:
- apiref
api_name:
- BcdObject.GetElementWithFlags
api_location:
- Root\WMI
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetElementWithFlags method of the BcdObject class

Gets the specified element. This method can be used to enumerate a qualified partition.

## Syntax


```mof
boolean GetElementWithFlags(
  [in]  ULONG      Type,
  [in]  ULONG      Flags,
  [out] BcdElement Element
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the values from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be zero or the following value.



| Value                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Qualified"></span><span id="qualified"></span><span id="QUALIFIED"></span><dl> <dt>**Qualified**</dt> <dt>1</dt> </dl> | If this parameter is set and the element is on a partition, the method retrieves the specified element as a [**BcdDeviceQualifiedPartitionData**](bcddevicequalifiedpartitiondata.md) element. If the element is not on a partition, this parameter is ignored. <br/> |



 

If the *Flags* parameter is zero, this method retrieves the specified element as a [**BcdDevicePartitionData**](bcddevicepartitiondata.md) element or, if the disk is not present, as a [**BcdDeviceUnknownData**](bcddeviceunknowndata.md) element.

</dd> <dt>

*Element* \[out\]
</dt> <dd>

If the method succeeds, this parameter is set to the specified element.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





