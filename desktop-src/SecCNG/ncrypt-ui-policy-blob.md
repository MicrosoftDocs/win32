---
description: Used with the NCRYPT\_UI\_POLICY\_PROPERTY property to contain user interface information for a key.
ms.assetid: c567d8ba-3315-4316-8e09-93b2c10a55ec
title: NCRYPT_UI_POLICY_BLOB structure (Ncrypt\_provider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NCRYPT_UI_POLICY_BLOB
api_type: 
- HeaderDef
api_location: 
- Ncrypt_provider.h
---

# NCRYPT\_UI\_POLICY\_BLOB structure

The **NCRYPT\_UI\_POLICY\_BLOB** structure is used with the [**NCRYPT\_UI\_POLICY\_PROPERTY**](key-storage-property-identifiers.md) property to contain user interface information for a key.

## Syntax


```C++
typedef struct __NCRYPT_UI_POLICY_BLOB {
  DWORD dwVersion;
  DWORD dwFlags;
  DWORD cbCreationTitle;
  DWORD cbFriendlyName;
  DWORD cbDescription;
} NCRYPT_UI_POLICY_BLOB;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure. This member must contain 1.

</dd> <dt>

**dwFlags**
</dt> <dd>

A set of flags that provide additional user interface information or requirements.



| Value                                                                                                                                                                                                                                                                                                  | Meaning                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="NCRYPT_UI_PROTECT_KEY_FLAG"></span><span id="ncrypt_ui_protect_key_flag"></span><dl> <dt>**NCRYPT\_UI\_PROTECT\_KEY\_FLAG**</dt> <dt>0x00000001</dt> </dl>                                | Display the strong key user interface as needed.<br/> |
| <span id="NCRYPT_UI_FORCE_HIGH_PROTECTION_FLAG"></span><span id="ncrypt_ui_force_high_protection_flag"></span><dl> <dt>**NCRYPT\_UI\_FORCE\_HIGH\_PROTECTION\_FLAG**</dt> <dt>0x00000002</dt> </dl> | Force high protection.<br/>                           |



 

</dd> <dt>

**cbCreationTitle**
</dt> <dd>

The length, in bytes, of the creation title. The creation title is a null-terminated Unicode string that specifies the text that is used as the title of the strong key dialog box when the key is completed. The creation title must be placed immediately following the **NCRYPT\_UI\_POLICY\_BLOB** structure. If the value of the **cbCreationTitle** member is set to 0, a default creation title is used for the title of the strong key dialog box. This member is only used on key finalization.

</dd> <dt>

**cbFriendlyName**
</dt> <dd>

The length, in bytes, of the friendly name of the key. The friendly name is a null-terminated Unicode string that contains the text that is displayed in the strong key dialog box as the name of the key. The friendly name must be placed immediately following the creation title in this BLOB. If the value of the **cbFriendlyName** member is set to 0, a default name is used in the strong key dialog box. This member is used both when the key is completed and when the key is used.

</dd> <dt>

**cbDescription**
</dt> <dd>

The length, in bytes, of the key description. The key description is a null-terminated Unicode string that contains the text that is displayed in the strong key dialog box as the description of the key. The description value must be placed immediately following the friendly name in this BLOB. If the value of the **cbDescription** member is set to 0, a default description is used in the strong key dialog box. This member is used both when the key is completed and when the key is used.

</dd> </dl>

## Remarks

This structure is included in the Ncrypt\_provider.h header. To use the structure, you must download the [Cryptographic Provider Development Kit](/collaborate/connect-redirect?InvitationID=CSDK-GYTG-R2PX&ProgramID=7264) from Microsoft Connect.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                          |
| Header<br/>                   | <dl> <dt>Ncrypt\_provider.h</dt> </dl> |



 

