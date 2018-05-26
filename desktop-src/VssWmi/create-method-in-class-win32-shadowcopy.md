---
title: Create method of the Win32\_ShadowCopy class
description: The Create method creates a shadow copy using the specified context.
ms.assetid: 62ba9405-108b-4025-9355-e637d52107ab
keywords:
- Create method
- Create method, Win32_ShadowCopy class
- Win32_ShadowCopy class, Create method
topic_type:
- apiref
api_name:
- Win32_ShadowCopy.Create
api_location:
- Vsswmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create method of the Win32\_ShadowCopy class

The **Create** method creates a shadow copy using the specified context.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Create(
  [in]  string Volume,
  [in]  string Context = "ClientAccessible",
  [out] string ShadowID
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

Volume used for the shadow copy. This volume is sometimes referred to as the original volume. The *Volume* parameter can be specified as a volume drive letter, mount point, or volume globally unique identifier (GUID) name.

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Context that the provider uses when creating the shadow. The default is "ClientAccessible".

</dd> <dt>

*ShadowID* \[out\]
</dt> <dd>

Unique identifier that identifies this shadow copy.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                                      |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success.<br/>                                              |
| <dl> <dt>**1**</dt> </dl>  | Access denied.<br/>                                        |
| <dl> <dt>**2**</dt> </dl>  | Invalid argument.<br/>                                     |
| <dl> <dt>**3**</dt> </dl>  | Specified volume not found.<br/>                           |
| <dl> <dt>**4**</dt> </dl>  | Specified volume not supported.<br/>                       |
| <dl> <dt>**5**</dt> </dl>  | Unsupported shadow copy context.<br/>                      |
| <dl> <dt>**6**</dt> </dl>  | Insufficient storage.<br/>                                 |
| <dl> <dt>**7**</dt> </dl>  | Volume is in use.<br/>                                     |
| <dl> <dt>**8**</dt> </dl>  | Maximum number of shadow copies reached.<br/>              |
| <dl> <dt>**9**</dt> </dl>  | Another shadow copy operation is already in progress.<br/> |
| <dl> <dt>**10**</dt> </dl> | Shadow copy provider vetoed the operation.<br/>            |
| <dl> <dt>**11**</dt> </dl> | Shadow copy provider not registered.<br/>                  |
| <dl> <dt>**12**</dt> </dl> | Shadow copy provider failure.<br/>                         |
| <dl> <dt>**13**</dt> </dl> | Unknown error.<br/>                                        |



 

## Remarks

The **Create** method uses the same process used when manually creating a snapshot from the "Shadow Copies" dialog. If your scheduled snapshots fail, while your manual snapshots work, you can use this method to work around that issue.

## Examples

The following Jscript sample takes a snapshot of a volume that's already been configured with a VSS storage volume.


```JScript
var Win32_ShadowCopy = GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy");

Win32_ShadowCopy.Create(
  "C:\\",
  "ClientAccessible"
);
```



The following PowerShell code creates a shadow copy.


```PowerShell
# get existing shadow copies
$shadow = get-wmiobject win32_shadowcopy
"There are {0} shadow copies on this sytem" -f $shadow.count
""

# get static method
$class=[WMICLASS]"root\cimv2:win32_shadowcopy"

# create a new shadow copy
"Creating a new shadow copy"
$class.create("C:\", "ClientAccessible")

# Count again
$shadow = get-wmiobject win32_shadowcopy
"There are now {0} shadow copies on this sytem" -f $shadow.count

```



The previous code sample returns the following information:

``` syntax
There are 8 shadow copies on this sytem

Creating a new shadow copy
  
__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     :
__DYNASTY        : __PARAMETERS
__RELPATH        :
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         :
__NAMESPACE      :
__PATH           :
ReturnValue      : 0
ShadowID         : {18BDD207-FB1B-4860-B918-B94C9EBF1F1F}

There are now 9 shadow copies on this sytem
```

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vss.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vsswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ShadowCopy**](win32-shadowcopy.md)
</dt> </dl>

 

 





