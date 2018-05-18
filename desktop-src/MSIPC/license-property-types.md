---
title: License property types
description: Constants used to refer to license properties when calling IpcGetLicenseProperty, IpcGetSerializedLicenseProperty or IpcSetLicenseProperty.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '553CDB31-F7AC-4BFA-B34A-D5D113A6557A'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_LI_VALIDITY_TIME
- IPC_LI_INTERVAL_TIME
- IPC_LI_OWNER
- IPC_LI_USER_RIGHTS_LIST
- IPC_LI_APP_SPECIFIC_DATA
- IPC_LI_DEPRECATED_ENCRYPTION_ALGORITHMS
- IPC_LI_CONNECTION_INFO
- IPC_LI_DESCRIPTOR
- IPC_LI_REFERRAL_INFO_URL
- IPC_LI_CONTENT_KEY
- IPC_LI_CONTENT_ID
- IPC_LI_APP_SPECIFIC_DATA_NO_ENCRYPTION
- IPC_LI_ISSUED_TIME
- IPC_LI_AUTO_GRANT_OWNER_FULL_ACCESS
- IPC_LI_PREFERRED_ENCRYPTION_PACKAGE
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# License property types

Constants used to refer to license properties when calling [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md), [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) or [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md).

<dl> <dt>

<span id="IPC_LI_VALIDITY_TIME"></span><span id="ipc_li_validity_time"></span>**IPC\_LI\_VALIDITY\_TIME**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Specifies the time period over which a license is valid. The property is represented as an [**IPC\_TERM**](ipc-term.md) structure.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **PCIPC\_TERM**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_TERM**\*.

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_INTERVAL_TIME"></span><span id="ipc_li_interval_time"></span>**IPC\_LI\_INTERVAL\_TIME**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Specifies the time period, in days, over which a license may be used to decrypt content without having to renew the license request from the server. The property is represented as an **LDPWORD** type.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **LPDWORD**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **LPDWORD**\*.

> \[!Important\]  
>
> -   The maximum permitted value for the time interval is 65535.
> -   Setting the value to 0 will require the application to connect to the server each time content is consumed.
> -   If this value is not set in the license, [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) will return **IPCERROR\_LICENSE\_INTERVAL\_TIME\_NOT\_SET**.

 

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_OWNER"></span><span id="ipc_li_owner"></span>**IPC\_LI\_OWNER**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Specifies the license owner. The property is represented as an [**IPC\_USER**](ipc-user.md) structure.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **PCIPC\_USER**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_USER**\*.

This property cannot be deleted with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md). If the *fDelete* parameter is specified with this property, **IpcSetLicenseProperty** will return **E\_INVALIDARG**.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_USER_RIGHTS_LIST"></span><span id="ipc_li_user_rights_list"></span>**IPC\_LI\_USER\_RIGHTS\_LIST**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Specifies a user rights list. The property is represented as an [**IPC\_USER\_RIGHTS\_LIST**](ipc-user-rights-list.md) structure.

Your application should explicitly add "owner" rights when creating a license from scratch using [**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md). For more information see, [Add explicit owner rights](add-explicit-owner-rights.md).

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **PCIPC\_USER\_RIGHTS\_LIST**.

This property cannot be deleted with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md). If the *fDelete* parameter is specified with this property, **IpcSetLicenseProperty** will return **E\_INVALIDARG**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_USER\_RIGHTS\_LIST**\*.

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_APP_SPECIFIC_DATA"></span><span id="ipc_li_app_specific_data"></span>**IPC\_LI\_APP\_SPECIFIC\_DATA**
</dt> <dd> <dl> <dt>

5
</dt> <dt>



Specifies application-defined properties of the license that can be used for additional logging. The properties are represented as an [**IPC\_NAME\_VALUE\_LIST**](ipc-name-value-list.md) structure.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **PCIPC\_NAME\_VALUE\_LIST**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_NAME\_VALUE\_LIST**\*.

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_DEPRECATED_ENCRYPTION_ALGORITHMS"></span><span id="ipc_li_deprecated_encryption_algorithms"></span>**IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS**
</dt> <dd> <dl> <dt>

6
</dt> <dt>



Specifies whether deprecated encryption algorithms should be used. The property is a **BOOL** value that is **TRUE** if deprecated algorithms should be used; **FALSE** otherwise.

This property should only be used by applications that protect content that will be consumed by AD RMS applications built using the MSDRM library (for more information, see [AD RMS Functions](https://msdn.microsoft.com/library/bb204612).

Setting this property to **TRUE**:

-   Allows you to generate licenses compatible with the MSDRM library.
-   May cause your application to protect content in a way that does not conform to your customers' standards for content protection.
-   Will prevent your application from benefitting from any cryptographic enhancements added to RMS SDK 2.1 going forward.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *ppvProperty* parameter is a pointer to type **const BOOL**.

This property cannot be deleted with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md). If the *fDelete* parameter is specified with this property, **IpcSetLicenseProperty** will return **E\_INVALIDARG**.

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.

> [!Note]  
> License buffer data is encoded in UTF8 when using the default flags and UTF16 when using the **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** flag.

 


</dt> </dl> </dd> <dt>

<span id="IPC_LI_CONNECTION_INFO"></span><span id="ipc_li_connection_info"></span>**IPC\_LI\_CONNECTION\_INFO**
</dt> <dd> <dl> <dt>

7
</dt> <dt>



Specifies the connection info of the server that issues this license. The property is represented as an [**IPC\_CONNECTION\_INFO**](ipc-connection-info.md) structure. This property is only used for querying, and cannot be used with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md).

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_CONNECTION\_INFO**\*.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_DESCRIPTOR"></span><span id="ipc_li_descriptor"></span>**IPC\_LI\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

8
</dt> <dt>



Specifies a language-specific name and description from the license. The property is represented as an [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structure.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md):

-   The *pvProperty* parameter is of type **PCIPC\_TEMPLATE\_INFO**.
-   The **IPC\_TEMPLATE\_INFO::wszID** field is not required and is ignored.
-   These members of [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) are read-only:

    -   **wszIssuerDisplayName**
    -   **fFromTemplate**

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **PIPC\_TEMPLATE\_INFO**\*. The **IPC\_TEMPLATE\_INFO::wszID** field is returned as **NULL** if **IPC\_TEMPLATE\_INFO::fFromTemplate** is **FALSE**.

When using this property with the [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md) function, the *hKey* parameter is required.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_REFERRAL_INFO_URL"></span><span id="ipc_li_referral_info_url"></span>**IPC\_LI\_REFERRAL\_INFO\_URL**
</dt> <dd> <dl> <dt>

10
</dt> <dt>



Specifies an application defined URL where a user can get additional information to access the content.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **LPCWSTR**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvProperty* parameter is of type **LPWSTR**\*.

If referral information is not set in the license, a default value will be returned.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_CONTENT_KEY"></span><span id="ipc_li_content_key"></span>**IPC\_LI\_CONTENT\_KEY**
</dt> <dd> <dl> <dt>

11
</dt> <dt>



Specifies that this license should reuse an existing key for protecting the content. Existing content republished this way does not need to be re-encrypted by using [**IpcEncrypt**](ipcencrypt.md) if the underlying content has not changed.

The **IPC\_LI\_DEPRECATED\_ENCRYPTION\_ALGORITHMS** property may not be used in conjunction with this property.

This property cannot be deleted with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md). If the *fDelete* parameter is specified with this property, **IpcSetLicenseProperty** will return **E\_INVALIDARG**.

This is not a valid license property for [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md).

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* is of type **IPC\_KEY\_HANDLE**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md), the *ppvProperty* is of type **PIPC\_KEY\_HANDLE**. This should be closed with [**IpcCloseHandle**](ipcclosehandle.md).


</dt> </dl> </dd> <dt>

<span id="IPC_LI_CONTENT_ID"></span><span id="ipc_li_content_id"></span>**IPC\_LI\_CONTENT\_ID**
</dt> <dd> <dl> <dt>

12
</dt> <dt>



Specifies unique Id of the content.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvProperty* parameter is of type **LPWSTR**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *ppvLicenseInfo* is of type **LPWSTR\***.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_APP_SPECIFIC_DATA_NO_ENCRYPTION"></span><span id="ipc_li_app_specific_data_no_encryption"></span>**IPC\_LI\_APP\_SPECIFIC\_DATA\_NO\_ENCRYPTION**
</dt> <dd> <dl> <dt>

13
</dt> <dt>



Specifies application defined properties of the license, that can be used for additional logging. This information will not be part of encrypted rights in license.

Since it will be in the clear, its not recommended that you put any sensitive information in this data.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvLicenseInfo* is of type **PCIPC\_NAME\_VALUE\_LIST**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *pvLicenseInfo* is of type **PIPC\_NAME\_VALUE\_LIST\***.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_ISSUED_TIME"></span><span id="ipc_li_issued_time"></span>**IPC\_LI\_ISSUED\_TIME**
</dt> <dd> <dl> <dt>

14
</dt> <dt>



Specifies the issued time of the license. This property is only used for querying and cannot be used with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md).

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) and [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), the *pvLicenseInfo* is of type **FILETIME\***.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_AUTO_GRANT_OWNER_FULL_ACCESS"></span><span id="ipc_li_auto_grant_owner_full_access"></span>**IPC\_LI\_AUTO\_GRANT\_OWNER\_FULL\_ACCESS**
</dt> <dd> <dl> <dt>

15
</dt> <dt>



Specifies whether the SDK should automatically grant the owner full access when the access control list does not have an entry for the owner.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), the *pvLicenseInfo* parameter is of type **BOOL**.

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md), the *ppvLicenseInfo* parameter is of type **PBOOL\***.


</dt> </dl> </dd> <dt>

<span id="IPC_LI_PREFERRED_ENCRYPTION_PACKAGE"></span><span id="ipc_li_preferred_encryption_package"></span>**IPC\_LI\_PREFERRED\_ENCRYPTION\_PACKAGE**
</dt> <dd> <dl> <dt>


</dt> <dt>



Sets the preferred encryption package.

For [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), *pvLicenseInfo* parameter is of type **LPDWORD\***

For [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md), *ppvLicenseInfo* parameter is of type **LPDWORD**.

For constants used to set the encryption package, see [**Preferred encryption**](preferred-encryption.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





