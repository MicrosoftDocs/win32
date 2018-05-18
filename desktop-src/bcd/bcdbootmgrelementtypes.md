---
title: BcdBootMgrElementTypes enumeration
description: Specifies the boot manager element types. For more details on the layout of this enumeration, see BcdElementType.
ms.assetid: 'e7c42cef-85f2-4f40-9aee-cf51f49ae030'
keywords: ["BcdBootMgrElementTypes enumeration Boot Config"]
topic_type:
- apiref
api_name:
- BcdBootMgrElementTypes
api_type:
- NA
---

# BcdBootMgrElementTypes enumeration

Specifies the boot manager element types. For more details on the layout of this enumeration, see [**BcdElementType**](bcdelementtype.md).

## Syntax


```C++
typedef enum BcdBootMgrElementTypes { 
  BcdBootMgrObjectList_DisplayOrder            = 0x24000001,
  BcdBootMgrObjectList_BootSequence            = 0x24000002,
  BcdBootMgrObject_DefaultObject               = 0x23000003,
  BcdBootMgrInteger_Timeout                    = 0x25000004,
  BcdBootMgrBoolean_AttemptResume              = 0x26000005,
  BcdBootMgrObject_ResumeObject                = 0x23000006,
  BcdBootMgrObjectList_ToolsDisplayOrder       = 0x24000010,
  BcdBootMgrBoolean_DisplayBootMenu            = 0x26000020,
  BcdBootMgrBoolean_NoErrorDisplay             = 0x26000021,
  BcdBootMgrDevice_BcdDevice                   = 0x21000022,
  BcdBootMgrString_BcdFilePath                 = 0x22000023,
  BcdBootMgrBoolean_ProcessCustomActionsFirst  = 0x26000028,
  BcdBootMgrIntegerList_CustomActionsList      = 0x27000030,
  BcdBootMgrBoolean_PersistBootSequence        = 0x26000031
} BcdBootMgrElementTypes;
```



## Constants

<dl> <dt>

<span id="BcdBootMgrObjectList_DisplayOrder"></span><span id="bcdbootmgrobjectlist_displayorder"></span><span id="BCDBOOTMGROBJECTLIST_DISPLAYORDER"></span>**BcdBootMgrObjectList\_DisplayOrder**
</dt> <dd>

The order in which BCD objects should be displayed. Objects are displayed using the string specified by the **BcdLibraryString\_Description** element. The element data format is [**BcdObjectListElement**](bcdobjectlistelement.md).

</dd> <dt>

<span id="BcdBootMgrObjectList_BootSequence"></span><span id="bcdbootmgrobjectlist_bootsequence"></span><span id="BCDBOOTMGROBJECTLIST_BOOTSEQUENCE"></span>**BcdBootMgrObjectList\_BootSequence**
</dt> <dd>

List of boot environment applications the boot manager should execute. The applications are executed in the order they appear in this list. The element data format is [**BcdObjectListElement**](bcdobjectlistelement.md).

If the firmware boot manager does not support loading multiple applications, this list cannot contain more than one entry.

</dd> <dt>

<span id="BcdBootMgrObject_DefaultObject"></span><span id="bcdbootmgrobject_defaultobject"></span><span id="BCDBOOTMGROBJECT_DEFAULTOBJECT"></span>**BcdBootMgrObject\_DefaultObject**
</dt> <dd>

The default boot environment application to load if the user does not select one. The element data format is [**BcdObjectElement**](bcdobjectelement.md).

</dd> <dt>

<span id="BcdBootMgrInteger_Timeout"></span><span id="bcdbootmgrinteger_timeout"></span><span id="BCDBOOTMGRINTEGER_TIMEOUT"></span>**BcdBootMgrInteger\_Timeout**
</dt> <dd>

The maximum number of seconds a boot selection menu is to be displayed to the user. The menu is displayed until the user selects an option or the time-out expires. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the boot manager waits for the user to make a selection.

</dd> <dt>

<span id="BcdBootMgrBoolean_AttemptResume"></span><span id="bcdbootmgrboolean_attemptresume"></span><span id="BCDBOOTMGRBOOLEAN_ATTEMPTRESUME"></span>**BcdBootMgrBoolean\_AttemptResume**
</dt> <dd>

Indicates that a resume operation should be attempted during a system restart. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdBootMgrObject_ResumeObject"></span><span id="bcdbootmgrobject_resumeobject"></span><span id="BCDBOOTMGROBJECT_RESUMEOBJECT"></span>**BcdBootMgrObject\_ResumeObject**
</dt> <dd>

The resume application object. The element data format is [**BcdObjectElement**](bcdobjectelement.md).

</dd> <dt>

<span id="BcdBootMgrObjectList_ToolsDisplayOrder"></span><span id="bcdbootmgrobjectlist_toolsdisplayorder"></span><span id="BCDBOOTMGROBJECTLIST_TOOLSDISPLAYORDER"></span>**BcdBootMgrObjectList\_ToolsDisplayOrder**
</dt> <dd>

The boot manager tools display order list. The element data format is [**BcdObjectListElement**](bcdobjectlistelement.md).

</dd> <dt>

<span id="BcdBootMgrBoolean_DisplayBootMenu"></span><span id="bcdbootmgrboolean_displaybootmenu"></span><span id="BCDBOOTMGRBOOLEAN_DISPLAYBOOTMENU"></span>**BcdBootMgrBoolean\_DisplayBootMenu**
</dt> <dd>

Forces the display of the legacy boot menu, regardless of the number of OS entries in the BCD store and their **BcdOSLoaderInteger\_BootMenuPolicy**. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdBootMgrBoolean_NoErrorDisplay"></span><span id="bcdbootmgrboolean_noerrordisplay"></span><span id="BCDBOOTMGRBOOLEAN_NOERRORDISPLAY"></span>**BcdBootMgrBoolean\_NoErrorDisplay**
</dt> <dd>

Indicates whether the display of errors should be suppressed. If this setting is enabled, the boot manager exits to the multi-OS menu on OS launch error. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdBootMgrDevice_BcdDevice"></span><span id="bcdbootmgrdevice_bcddevice"></span><span id="BCDBOOTMGRDEVICE_BCDDEVICE"></span>**BcdBootMgrDevice\_BcdDevice**
</dt> <dd>

The device on which the boot application resides. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdBootMgrString_BcdFilePath"></span><span id="bcdbootmgrstring_bcdfilepath"></span><span id="BCDBOOTMGRSTRING_BCDFILEPATH"></span>**BcdBootMgrString\_BcdFilePath**
</dt> <dd>

The boot application. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdBootMgrBoolean_ProcessCustomActionsFirst"></span><span id="bcdbootmgrboolean_processcustomactionsfirst"></span><span id="BCDBOOTMGRBOOLEAN_PROCESSCUSTOMACTIONSFIRST"></span>**BcdBootMgrBoolean\_ProcessCustomActionsFirst**
</dt> <dd>

Controls whether custom actions are processed before a boot sequence. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> <dt>

<span id="BcdBootMgrIntegerList_CustomActionsList"></span><span id="bcdbootmgrintegerlist_customactionslist"></span><span id="BCDBOOTMGRINTEGERLIST_CUSTOMACTIONSLIST"></span>**BcdBootMgrIntegerList\_CustomActionsList**
</dt> <dd>

For more information see [Custom Bootstrap Actions in Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=258258). The element data format is [**BcdIntegerListElement**](bcdintegerlistelement.md).

</dd> <dt>

<span id="BcdBootMgrBoolean_PersistBootSequence"></span><span id="bcdbootmgrboolean_persistbootsequence"></span><span id="BCDBOOTMGRBOOLEAN_PERSISTBOOTSEQUENCE"></span>**BcdBootMgrBoolean\_PersistBootSequence**
</dt> <dd>

Controls whether a boot sequence persists across multiple boots. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdObjectElement**](bcdobjectelement.md)
</dt> <dt>

[**BcdObjectListElement**](bcdobjectlistelement.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> <dt>

[**BcdElementType**](bcdelementtype.md)
</dt> </dl>

 

 





