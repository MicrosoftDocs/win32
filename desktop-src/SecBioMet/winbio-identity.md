---
title: WINBIO\_IDENTITY structure
description: Contains an identifying value associated with a biometric template.
ms.assetid: '58a5f4ba-2f58-466c-90fd-9480c3c095db'
keywords: ["WINBIO_IDENTITY structure Windows Biometric Framework API"]
topic_type:
- apiref
api_name:
- WINBIO_IDENTITY
api_location:
- Winbio_types.h
api_type:
- HeaderDef
---

# WINBIO\_IDENTITY structure

The **WINBIO\_IDENTITY** structure contains an identifying value associated with a biometric template.

## Syntax


```C++
typedef struct _WINBIO_IDENTITY {
  WINBIO_IDENTITY_TYPE Type;
  union {
    ULONG  Null;
    ULONG  Wildcard;
    GUID   TemplateGuid;
    struct {
      ULONG Size;
      UCHAR Data[SECURITY_MAX_SID_SIZE];
    } AccountSid;
  } Value;
} WINBIO_IDENTITY;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Specifies the format of the identity information contained in this structure. This can be one of the following values:



| Value                                                                                                                                                                                         | Meaning                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="WINBIO_ID_TYPE_NULL"></span><span id="winbio_id_type_null"></span><dl> <dt>**WINBIO\_ID\_TYPE\_NULL**</dt> </dl>             | The template has no associated ID.<br/>                                   |
| <span id="WINBIO_ID_TYPE_WILDCARD"></span><span id="winbio_id_type_wildcard"></span><dl> <dt>**WINBIO\_ID\_TYPE\_WILDCARD**</dt> </dl> | The structure matches all template identities.<br/>                       |
| <span id="WINBIO_ID_TYPE_GUID"></span><span id="winbio_id_type_guid"></span><dl> <dt>**WINBIO\_ID\_TYPE\_GUID**</dt> </dl>             | The structure contains a GUID associated with the template.<br/>          |
| <span id="WINBIO_ID_TYPE_SID"></span><span id="winbio_id_type_sid"></span><dl> <dt>**WINBIO\_ID\_TYPE\_SID**</dt> </dl>                | The structure contains the account SID associated with the template.<br/> |



 

</dd> <dt>

**Value**
</dt> <dd>

A union that can contain one of the following values:

<dl> <dt>

**Null**
</dt> <dd>

Contains 1 if the **Type** member is **WINBIO\_ID\_TYPE\_NULL**.

</dd> <dt>

**Wildcard**
</dt> <dd>

Contains 1 if the **Type** member is **WINBIO\_ID\_TYPE\_WILDCARD**.

</dd> <dt>

**TemplateGuid**
</dt> <dd>

Contains a 128-bit GUID value that identifies the template if the **Type** member is **WINBIO\_ID\_TYPE\_GUID**.

</dd> <dt>

**AccountSid**
</dt> <dd>

A structure that contains an account SID if the **Type** member is **WINBIO\_ID\_TYPE\_SID**.

<dl> <dt>

**Size**
</dt> <dd>

The number of characters in the SID.

</dd> <dt>

**Data**
</dt> <dd>

An array of unsigned characters that contain the SID. The current maximum size of the array is 68 characters.

</dd> </dl> </dd> </dl> </dd> </dl>

## Remarks

This structure is used in the following functions:

-   [**WinBioDeleteTemplate**](winbiodeletetemplate.md)
-   [**WinBioEnrollCommit**](winbioenrollcommit.md)
-   [**WinBioEnumEnrollments**](winbioenumenrollments.md)
-   [**WinBioGetCredentialState**](winbiogetcredentialstate.md)
-   [**WinBioIdentify**](winbioidentify.md)
-   [**WinBioRemoveCredential**](winbioremovecredential.md)
-   [**WinBioVerify**](winbioverify.md)
-   [**WinBioVerifyWithCallback**](winbioverifywithcallback.md)

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> </dl>

 

 





