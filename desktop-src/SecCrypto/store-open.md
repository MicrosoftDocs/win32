---
description: Opens a specified certificate store.
ms.assetid: d6f398b4-dba6-4d84-b5eb-3c7737d17a6e
title: Store.Open method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Store.Open
api_type:
- COM
api_location:
- Capicom.dll
---

# Store.Open method

\[The **Open** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Store Class**](/dotnet/api/system.security.cryptography.x509certificates.x509store?view=netcore-3.1&preserve-view=true) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1&preserve-view=true) namespace.\]

The **Open** method opens a specified [*certificate store*](../secgloss/c-gly.md). By default, the CAPICOM\_CURRENT\_USER\_STORE location and CAPICOM\_MY\_STORE store are opened as read-only.

## Syntax


```VB
Store.Open( _
  [ ByVal StoreLocation ], _
  [ ByVal StoreName ], _
  [ ByVal OpenMode ] _
)
```



## Parameters

<dl> <dt>

*StoreLocation* \[in, optional\]
</dt> <dd>

A value of the [CAPICOM\_STORE\_LOCATION](capicom-store-location.md) enumeration that indicates the location of the store to be opened. The default value is CAPICOM\_CURRENT\_USER\_STORE. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_ACTIVE_DIRECTORY_USER_STORE"></span><span id="capicom_active_directory_user_store"></span><dl> <dt>**CAPICOM\_ACTIVE\_DIRECTORY\_USER\_STORE**</dt> </dl> | The store is an Active Directory store. No error will be generated if an Active Directory store is opened as read/write, but any changes to the store will not be persisted. Certificates cannot be added to or removed from Active Directory stores.<br/>                   |
| <span id="CAPICOM_CURRENT_USER_STORE"></span><span id="capicom_current_user_store"></span><dl> <dt>**CAPICOM\_CURRENT\_USER\_STORE**</dt> </dl>                             | The store is a current user store. A current user store may be a read/write store. If it is, changes in the contents of the store are persisted.<br/>                                                                                                                        |
| <span id="CAPICOM_LOCAL_MACHINE_STORE"></span><span id="capicom_local_machine_store"></span><dl> <dt>**CAPICOM\_LOCAL\_MACHINE\_STORE**</dt> </dl>                          | The store is a local computer store. Local computer stores can be read/write stores only if the user has read/write permissions. If the user has read/write permissions and if the store is opened read/write, then changes in the contents of the store are persisted.<br/> |
| <span id="CAPICOM_MEMORY_STORE"></span><span id="capicom_memory_store"></span><dl> <dt>**CAPICOM\_MEMORY\_STORE**</dt> </dl>                                                | The store is a memory store. Any changes in the contents of the store are not persisted.<br/>                                                                                                                                                                                |
| <span id="CAPICOM_SMART_CARD_USER_STORE"></span><span id="capicom_smart_card_user_store"></span><dl> <dt>**CAPICOM\_SMART\_CARD\_USER\_STORE**</dt> </dl>                   | The store is the group of present smart cards. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                               |



 

</dd> <dt>

*StoreName* \[in, optional\]
</dt> <dd>

A string that contains the name of the system certificate store to be opened. The default value is CAPICOM\_MY\_STORE. If the store is opened from a web script, the backslash (\\) character is not allowed in the name. In addition to stores defined by the system, user-defined stores can be opened.

This parameter can be a user-defined store or one of the following system certificate stores.



| Value                                                                                                                                                                            | Meaning                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_CA_STORE"></span><span id="capicom_ca_store"></span><dl> <dt>**CAPICOM\_CA\_STORE**</dt> </dl>          | CA store. This store is used to store intermediate CA certificates.<br/>                        |
| <span id="CAPICOM_MY_STORE"></span><span id="capicom_my_store"></span><dl> <dt>**CAPICOM\_MY\_STORE**</dt> </dl>          | My store. This store is used for a user's personal certificates.<br/>                           |
| <span id="CAPICOM_OTHER_STORE"></span><span id="capicom_other_store"></span><dl> <dt>**CAPICOM\_OTHER\_STORE**</dt> </dl> | AddressBook store. This store is used to keep the certificates of others.<br/>                  |
| <span id="CAPICOM_ROOT_STORE"></span><span id="capicom_root_store"></span><dl> <dt>**CAPICOM\_ROOT\_STORE**</dt> </dl>    | Root store. This store is used to store the root CA and self-signed, trusted certificates.<br/> |



 

</dd> <dt>

*OpenMode* \[in, optional\]
</dt> <dd>

A value of the [CAPICOM\_STORE\_OPEN\_MODE](capicom-store-open-mode.md) enumeration that indicates the open mode of the store. The default value is CAPICOM\_STORE\_OPEN\_READ\_ONLY. If the store is opened from a web script, this value is forced to CAPICOM\_STORE\_OPEN\_EXISTING\_ONLY. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED"></span><span id="capicom_store_open_maximum_allowed"></span><dl> <dt>**CAPICOM\_STORE\_OPEN\_MAXIMUM\_ALLOWED**</dt> </dl> | Open the store in read/write mode if the user has read/write permissions; otherwise, open the store in read-only mode.<br/> |
| <span id="CAPICOM_STORE_OPEN_READ_ONLY"></span><span id="capicom_store_open_read_only"></span><dl> <dt>**CAPICOM\_STORE\_OPEN\_READ\_ONLY**</dt> </dl>                   | Open the store in read-only mode.<br/>                                                                                      |
| <span id="CAPICOM_STORE_OPEN_READ_WRITE"></span><span id="capicom_store_open_read_write"></span><dl> <dt>**CAPICOM\_STORE\_OPEN\_READ\_WRITE**</dt> </dl>                | Open the store in read/write mode.<br/>                                                                                     |



 

The following flags can be combined with the values in the previous table by using a logical-**OR** operation.



| Value                                                                                                                                                                                                                              | Meaning                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span id="CAPICOM_STORE_OPEN_EXISTING_ONLY"></span><span id="capicom_store_open_existing_only"></span><dl> <dt>**CAPICOM\_STORE\_OPEN\_EXISTING\_ONLY**</dt> </dl>          | Open existing stores only; do not create a new store. Introduced in CAPICOM 2.0.<br/> |
| <span id="CAPICOM_STORE_OPEN_INCLUDE_ARCHIVED"></span><span id="capicom_store_open_include_archived"></span><dl> <dt>**CAPICOM\_STORE\_OPEN\_INCLUDE\_ARCHIVED**</dt> </dl> | Include archived certificates when using the store. Introduced in CAPICOM 2.0.<br/>   |



 

Stores in some locations can be opened only in read-only mode. These include all stores in CAPICOM\_LOCAL\_MACHINE\_STORE for which the user does not have write permissions. Attempts to open a store as a read/write store without proper access and permissions will result in the failure of the **Open** method. Active Directory stores can be opened as a read/write store without failure of the **Open** method, but changes to the store will not be persisted.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If this method is called on a SmartCard store, additional SmartCard user interfaces may be invoked.

> [!IMPORTANT]
> When this method is called from a web script, the script needs to access digital certificates on the local computer. If you allow the script to access your digital certificates, the website from which the script is run will also gain access to any personal information stored in the certificates. The first time this method is called from a particular domain, a dialog box is generated in which the user must indicate whether access to the certificates should be allowed. Stores opened from a web script automatically force the CAPICOM\_STORE\_OPEN\_EXISTING\_ONLY flag.

 

If *StoreLocation* is **CAPICOM\_SMART\_CARD\_USER\_STORE**, *StoreName* is ignored. In this case, CAPICOM reads all certificates from all available readers that contain a smart card.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Store**](store.md)
</dt> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> <dt>

[**Close**](store-close.md)
</dt> </dl>

 

 
