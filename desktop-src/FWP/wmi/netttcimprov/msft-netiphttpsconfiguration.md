---
description: Provides configuration settings for the IP over HTTPS (IP-HTTPs) Tunneling Protocol.
ms.assetid: 2d5d5c2a-33d3-4a41-8624-db0ab7e86914
title: MSFT\_NetIPHttpsConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPHttpsConfiguration
- MSFT_NetIPHttpsConfiguration.ConfigurationType
- MSFT_NetIPHttpsConfiguration.Type
- MSFT_NetIPHttpsConfiguration.State
- MSFT_NetIPHttpsConfiguration.AuthMode
- MSFT_NetIPHttpsConfiguration.ServerURL
- MSFT_NetIPHttpsConfiguration.Profile
- MSFT_NetIPHttpsConfiguration.ProfileActivated
- MSFT_NetIPHttpsConfiguration.StrongCRLRequired
- MSFT_NetIPHttpsConfiguration.PolicyStore
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPHttpsConfiguration class

Provides configuration settings for the IP over HTTPS (IP-HTTPs) Tunneling Protocol.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetIPHttpsConfiguration : MSFT_NetSettingData
{
  uint32  ConfigurationType;
  uint32  Type;
  uint32  State;
  uint32  AuthMode;
  string  ServerURL;
  string  Profile;
  boolean ProfileActivated;
  boolean StrongCRLRequired;
  string  PolicyStore;
};
```

## Members

The **MSFT\_NetIPHttpsConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetIPHttpsConfiguration** class has these methods.



| Method                                                                      | Description                                                         |
|:----------------------------------------------------------------------------|:--------------------------------------------------------------------|
| [**AddCertBinding**](addcertbinding-msft-netiphttpsconfiguration.md)       | Adds a HTTP SSL certificate to the profile.<br/>              |
| [**DisableProfile**](disableprofile-msft-netiphttpsconfiguration.md)       | Turns off the manual activation of the IP-HTTPs profile.<br/> |
| [**EnableProfile**](enableprofile-msft-netiphttpsconfiguration.md)         | Activates the specified IP-HTTPs profile manually.<br/>       |
| [**RemoveCertBinding**](removecertbinding-msft-netiphttpsconfiguration.md) | Removes all HTTP SSL certificates from the profile.<br/>      |
| [**Rename**](rename-msft-netiphttpsconfiguration.md)                       | Renames the IP-HTTPs profile.<br/>                            |
| [**Reset**](reset-msft-netiphttpsconfiguration.md)                         | Resets the configuration of IP-HTTPs.<br/>                    |



 

### Properties

The **MSFT\_NetIPHttpsConfiguration** class has these properties.

<dl> <dt>

**AuthMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the server needs to authenticate the incoming IP-HTTPS client connections.



| Value                                                                                                                                                                                                                                           | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="None"></span><span id="none"></span><span id="NONE"></span><dl> <dt>**None**</dt> <dt>0</dt> </dl>                                 | The IP-HTTPS server does not authenticate IP-HTTPS clients. <br/>      |
| <span id="Certificates"></span><span id="certificates"></span><span id="CERTIFICATES"></span><dl> <dt>**Certificates**</dt> <dt>1</dt> </dl> | The IP-HTTPS server is required to authenticate IP-HTTPS clients.<br/> |



 

</dd> <dt>

**ConfigurationType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the configuration type of this instance.

<dl> <dt>

<span id="Local"></span><span id="local"></span><span id="LOCAL"></span>**Local** (0)
</dt> <dt>

<span id="GroupPolicy"></span><span id="grouppolicy"></span><span id="GROUPPOLICY"></span>**GroupPolicy** (1)
</dt> <dt>

<span id="ProfileGP"></span><span id="profilegp"></span><span id="PROFILEGP"></span>**ProfileGP** (2)
</dt> </dl>

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the policy store that stores this configuration object.

</dd> <dt>

**Profile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the friendly name of the profile.

</dd> <dt>

**ProfileActivated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the profile is active.

</dd> <dt>

**ServerURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates either the URL on which the server interface listens for HTTP(S) requests or the URL to which the client interface sends HTTP(S) requests.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the state of the interface.

<dl> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (0)
</dt> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (1)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (2)
</dt> </dl>

</dd> <dt>

**StrongCRLRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether to check if strong signatures are on a certificate revocation list (CRL).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of the interface.

<dl> <dt>

<span id="Client"></span><span id="client"></span><span id="CLIENT"></span>**Client** (0)
</dt> <dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>**Server** (1)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




