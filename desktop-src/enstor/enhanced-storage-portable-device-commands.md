---
title: Enhanced Storage Portable Device Commands
description: The following Windows Portable Devices Enhanced Storage authentication, certificate, and password silo commands are passed via the IEnhancedStorageSilo SendCommand method.
ms.assetid: b848a866-9fdf-4cb3-b289-6df5fc1bf723
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enhanced Storage Portable Device Commands

The following Windows Portable Devices Enhanced Storage authentication, certificate, and password silo commands are passed via the [**IEnhancedStorageSilo::SendCommand**](/windows/previous-versions/EhStorAPI/nf-ehstorapi-ienhancedstoragesilo-sendcommand?branch=master) method. For details regarding the properties utilized by these commands, see [Enhanced Storage Properties](enhanced-storage-properties.md).

## Authentication Silo Commands



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_SILO_IS_AUTHENTICATION_SILO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will return whether or not the silo is an authentication silo.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_IS_AUTHENTICATION_SILO <strong>[VT_BOOLEAN]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_SILO_GET_AUTHENTICATION_STATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will return the authentication state for the silo.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE <strong>[VT_UI4]</strong><br />
</dl> Possible values for ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE result include:<br/> <dl> UNKNOWN : Initial setting before PnP entry and the silo state is unknown.<br />
NO_AUTHENTICATION_REQUIRED: The silo has not been provisioned.<br />
NOT_AUTHENTICATED: The silo is not authenticated.<br />
AUTHENTICATED: The silo is authenticated.<br />
AUTHENTICATION_DENIED: Authentication was denied.<br />
DEVICE_ERROR: The silo timed out or a device error occurred.<br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_START_AUTHENTICATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will begin authentication for the silo. An application is required to register for callbacks in order to receive callbacks associated with authorization state changes.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_START_UNAUTHENTICATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will begin deauthentication for the silo. An application is required to register for callbacks in order to receive callbacks associated with authorization state changes.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_SILO_ENUMERATE_SILOS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access: Read/Write</td>
</tr>
<tr class="even">
<td>Parameters: <dl>[Required] ENHANCED_STORAGE_PROPERTY_QUERY_SILO_TYPE <strong>[VT_UI4]</strong><br />
</dl> Valid values for this parameter include:<br/> <dl> PDO_TYPE_DISK: Retrieve silo information for the disk.<br />
PDO_TYPE_THIS: Retrieve silo information for the silo handling this request.<br />
</dl></td>
</tr>
<tr class="odd">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_QUERY_SILO_RESULTS <strong>[VT_VECTOR | VT_U1]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 

## Certificate Silo Commands



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_HOST_CERTIFICATE_AUTHENTICATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will attempt to initiate a host authentication based on an HCh (or XCh) from the silo. If an index or certificate is specified, it will be used. The default behavior is to attempt authentication of all HCh or XCh certificates present on the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Optional] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_CERTIFICATE <strong>[VT_VECTOR | VT_UI1]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_DEVICE_CERIFICATE_AUTHENTICATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will attempt to initiate a device authentication. If an index or certificate is specified, it will be used. The certificate must be a ASCm or ASCh. The default behavior is to attempt authentication using the ASCm or all ASCh certificates present on the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Optional] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<tbody>
<tr class="odd">
<td>ENHANCED_STORAGE_COMMAND_CERT_ADMIN_CERTIFICATE_AUTHENTICATION</td>
</tr>
<tr class="even">
<td>This command will attempt to initiate an administrative authentication based on the PCp or XCp certificate on the silo.</td>
</tr>
<tr class="odd">
<td>Access: Read/Write</td>
</tr>
<tr class="even">
<td>Parameters: None</td>
</tr>
<tr class="odd">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_INITIALIZE_TO_MANUFACTURER_STATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will attempt to initialize the silo to the manufacturer state. This command requires a successful administrative authentication. If an administrative authentication has not yet been accomplished, the command will initiate an administrative authentication operation before initializing the silo to the manufacturer state.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE_COUNT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will retrieve the number of certificate slots as well as the number of certificates stored in the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT [VT_ERROR]<br />
ENHANCED_STORAGE_PROPERTY_MAX_CERTIFICATE_COUNT <strong>[VT_UINT]</strong><br />
ENHANCED_STORAGE_PROPERTY_STORED_CERTIFICATE_COUNT <strong>[VT_UINT]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_CERTIFICATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will return the certificate stored at the certificate index location. Index '0' is a special location that returns the ASCm chain in the PKCS7 format.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT [VT_ERROR]<br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_NEXT_CERTIFICATE_OF_TYPE_INDEX <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_LENGTH <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE <strong>[VT_UINT | VT_UI1]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_SET_CERTIFICATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will set a certificate to the certificate index location. This command requires administrative authentication.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_TYPE <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_VALIDATION_POLICY <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_SIGNER_CERTIFICATE_INDEX <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_CERTIFICATE <strong>[VT_UINT | VTUI1]</strong><br />
</dl>
<blockquote>
[!Note]<br />
The Validation Policy parameter is required if the certificate is of a type PCp or HCh. The Signer Certificate Index parameter is required if the certificate is of a type ASCh or SCh.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT [VT_ERROR]<br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_CREATE_CERTIFICATE_REQUEST</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command retrieves a certificate request from the silo. The returned certificate request can then be used to generate an ASCh certificate</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_REQUEST <strong>[VT_VECTOR | VT_UI1]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_UNAUTHENTICATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will reset the authentication state of the cert silo to the 'Initialized' state.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command retrieves a capability from the silo. Data returned is in the format native to the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_CAPABILITY_TYPE <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT [VT_ERROR]<br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITY <strong>[VT_VECTOR | VT_UI1]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_CAPABILITIES</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command retrieves all capabilities from a silo as a collection.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters:None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_CAPABILITIES <strong>[VT_UNKNOWN]</strong><dl> ENHANCED_STORAGE_CAPABILITY_HASH_ALGS <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_CAPABILITY_SIGNING_AGLS <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_CAPABILITY_RENDER_USER_DATA_UNUSABLE <strong>[VT_BOOL]</strong><br />
ENHANCED_STORAGE_CAPABILITY_CERTIFICATE_EXTENSION_PARSING <strong>[VT_BOOL]</strong><br />
</dl> </dd> </dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_ACT_FRIENDLY_NAME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command retrieves the friendly name of the ACT containing the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters:None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_CERTIFICATE_ACT_FRIENDLY_NAME <strong>[VT_LPWSTR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_CERT_GET_SILO_GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command will retrieve the GUID associated with the silo.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters:None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_CERTIFICATE_SILO_GUID <strong>[VT_LPWSTR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 

## Password Silo Commands



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_AUTHORIZE_ACT_ACCESS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command attempts to authenticate to the silo for access to the data in the ACT.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_UNAUTHORIZE_ACT_ACCESS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command attempts to deauthenticate to the silo for access to the data in the ACT.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Optional] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_QUERY_INFORMATION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command queries the current silo password information.</td>
</tr>
<tr class="even">
<td>Access: Read</td>
</tr>
<tr class="odd">
<td>Parameters: None</td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
ENHANCED_STORAGE_PROPERTY_AUTHENTICATION_STATE <strong>[VT_UI4]</strong><br />
ENHANCED_STORAGE_PROPERTY_PASSWORD_SILO_INFO <strong>[VT_VECTOR | VT_U1]</strong><br />
ENHANCED_STORAGE_PROPERTY_ADMIN_HINT <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_PROPERTY_USER_HINT <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_PROPERTY_USER_NAME <strong>[VT_LPWSTR]</strong><br />
ENHANCED_STORAGE_PROPERTY_SILO_NAME <strong>[VT_LPWSTR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_CONFIG_ADMINISTRATOR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command configures the administrator account.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES <strong>[VT_UI4]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_FRIENDLYNAME_SPECIFIED <strong>[VT_UI4]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_SILO_NAME <strong>[VT_LPWSTR]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_CREATE_USER</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command creates a user account.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters:<dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_USER_HINT <strong>[VT_LPWSTR]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_USER_NAME <strong>[VT_LPWSTR]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_MAX_AUTH_FAILURES <strong>[VT_UI4]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_DELETE_USER</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command deletes a user account.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_CHANGE_PASSWORD</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command changes the password for an administrator or user account.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD_INDICATOR <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD_INDICATOR <strong>[VT_UI4]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_ADMIN_HINT <strong>[VT_LPWSTR]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_USER_HINT <strong>[VT_LPWSTR]</strong><br />
[Optional] ENHANCED_STORAGE_PROPERTY_SECURITY_IDENTIFIER <strong>[VT_VECTOR | VT_U1]</strong><br />
</dl>
<blockquote>
[!Note]<br />
While this command must be provided with either a User Hint or Admin password hint, only one of these may be specified per operation.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_INITIALIZE_USER_PASSWORD</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command initializes an existing user password.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Required] ENHANCED_STORAGE_PROPERTY_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_NEW_PASSWORD <strong>[VT_VECTOR | VT_U1]</strong><br />
[Required] ENHANCED_STORAGE_PROPERTY_NEW_HINT <strong>[VT_LPWSTR]</strong><br />
</dl></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ENHANCED_STORAGE_COMMAND_PASSWORD_START_INITIALIZE_TO_MANUFACTURER_STATE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This command starts the initialization of the silo to the manufacturer state.</td>
</tr>
<tr class="even">
<td>Access: Read/Write</td>
</tr>
<tr class="odd">
<td>Parameters: <dl>[Optional] ENHANCED_STORAGE_SECURITY_IDENTIFIER <strong>[VT_VECTOR | VT_U1]</strong><br />
</dl>
<blockquote>
[!Note]<br />
Depending on silo implementation, this parameter may be required in some scenarios.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Results: <dl> WPD_PROPERTY_COMMON_HRESULT <strong>[VT_ERROR]</strong><br />
</dl></td>
</tr>
</tbody>
</table>



 

 

 





