---
title: AppID Key
description: Groups the configuration options for one or more DCOM objects into one centralized location in the registry. DCOM objects hosted by the same executable are grouped into one AppID to simplify the management of common security and configuration settings.
ms.assetid: 4e3d8c87-e6d7-4b4d-8f72-7180be1e51cf
keywords:
- AppID registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# AppID Key

Groups the configuration options for one or more DCOM objects into one centralized location in the registry. DCOM objects hosted by the same executable are grouped into one AppID to simplify the management of common security and configuration settings.

## Registry Key

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\AppID**\\*{*AppID\_GUID*}*



| Registry value                                           | Description                                                                                                                                                                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessPermission**](accesspermission.md)             | Describes the Access Control List (ACL) of the principals that can access instances of this class. This ACL is used only by applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). |
| [**ActivateAtStorage**](activateatstorage.md)           | Configures the client to instantiate objects on the same computer as the persistent state they are using or from which they are initialized.                                                                    |
| [**AppID**](appid.md)                                   | Identifies the AppID GUID that corresponds to the named executable.                                                                                                                                             |
| [**AppIDFlags**](appidflags.md)                         | Configures how a COM server that is configured to run as the "Interactive User" will be launched or bound to by a client in a non-default desktop.                                                              |
| [**AuthenticationLevel**](authenticationlevel.md)       | Sets the authentication level for applications that do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or for applications that call **CoInitializeSecurity** and specify an AppID.               |
| [**DllSurrogate**](dllsurrogate.md)                     | Enables DLL servers to run in a surrogate process. If an empty string is specified, the system-supplied surrogate is used; otherwise, the value specifies the path of the surrogate to be used.                 |
| [**DllSurrogateExecutable**](dllsurrogateexecutable.md) | Enables DLL servers to run in a custom surrogate process, in conjunction with the [**DllSurrogate**](dllsurrogate.md) registry value.                                                                          |
| [**Endpoints**](endpoints.md)                           | Configures a COM application to use a specified TCP port number for DCOM communications.                                                                                                                        |
| [**LaunchPermission**](launchpermission.md)             | Describes the Access Control List (ACL) of the principals that can start new servers for this class.                                                                                                            |
| [**LoadUserSettings**](loadusersettings.md)             | Determines whether COM will load the user profile for COM servers running as the launching user application identity.                                                                                           |
| [**LocalService**](localservice.md)                     | Installs an object as a service application.                                                                                                                                                                    |
| [**PreferredServerBitness**](preferredserverbitness.md) | Sets the preferred architecture, 32-bit or 64-bit, for this COM server.                                                                                                                                         |
| [**RemoteServerName**](remoteservername.md)             | Configures the client to request the object be run at a particular computer whenever an activation function is called for which a [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure is not specified.              |
| [**ROTFlags**](rotflags.md)                             | Controls the registration of a COM server in the running object table (ROT).                                                                                                                                    |
| [**RunAs**](runas.md)                                   | Configures a class to run under a specific user account when activated by a remote client without being written as a service application.                                                                       |
| [**ServiceParameters**](serviceparameters.md)           | Specifies the command-line parameters to be passed to an object installed for use by COM through the [**LocalService**](localservice.md) registry value.                                                       |
| [**SRPTrustLevel**](srptrustlevel.md)                   | Sets the software restriction policy (SRP) trust level for applications.                                                                                                                                        |



 

## Remarks

AppIDs are mapped to executables and classes using two different mechanisms:

-   Using a 128-bit Globally Unique Identifier (GUID) that identifies the **AppID** key. A class indicates its corresponding AppID under the [**CLSID**](clsid-key-hklm.md) key in a named value "AppID". This mapping is used during activation.
-   Using a named value that indicates an executable name (such as "MYOLDAPP.EXE"). This named value is of type **REG\_SZ** and contains the string representation of the AppID associated with the executable. This mapping is used to obtain the default access permissions and authentication level.

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

For COM servers, the mapping is usually generated and written to the registry during the registration process or when running dcomcnfg.exe. However, COM clients that want to set security using the **AppID** key must create appropriate registry keys and specify the required mapping by calling the [registry functions](/windows/desktop/SysInfo/registry-functions) or using Regedit.exe. Then values such as [**AccessPermission**](accesspermission.md) or [**AuthenticationLevel**](authenticationlevel.md) can be set for the client. For example, suppose the name of your executable for your client process is "YourClient.exe" and you want to set the authentication level to "None". You would use Guidgen.exe or Uuidgen.exe to create the GUID that is the AppID for your executable. Then you would set values in the registry as shown in the following example, where 00000001 represents an authentication level of "None":

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {MyGuid}
      AuthenticationLevel = 00000001
   MyClient.exe
      AppID = {MyGUID}
```

 

 