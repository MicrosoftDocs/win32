---
title: NetworkControllerApplicationConfiguration class
description: Contains the network controller application configuration data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e2173d76-e5cd-4ad4-af3c-9dc76cab499d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NetworkControllerApplicationConfiguration class
- NetworkControllerApplicationConfiguration class, described
topic_type:
- apiref
api_name:
- NetworkControllerApplicationConfiguration
- NetworkControllerApplicationConfiguration.Version
- NetworkControllerApplicationConfiguration.RestClientAuthentication
- NetworkControllerApplicationConfiguration.RestClientCertThumbprints
- NetworkControllerApplicationConfiguration.RestClientSecurityGroupName
- NetworkControllerApplicationConfiguration.NodeList
- NetworkControllerApplicationConfiguration.RestIPAddress
- NetworkControllerApplicationConfiguration.SslCertificateRawData
- NetworkControllerApplicationConfiguration.IsApplicationLogEnabled
- NetworkControllerApplicationConfiguration.RestURL
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NetworkControllerApplicationConfiguration class

Contains the network controller application configuration data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerApplicationConfiguration
{
  string                               Version;
  string                               RestClientAuthentication;
  string                               RestClientCertThumbprints[];
  string                               RestClientSecurityGroupName;
  NetworkControllerNodeApplicationInfo NodeList[];
  string                               RestIPAddress;
  uint8                                SslCertificateRawData[];
  boolean                              IsApplicationLogEnabled;
  string                               RestURL;
};
```

## Members

The **NetworkControllerApplicationConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerApplicationConfiguration** class has these properties.

<dl> <dt>

**IsApplicationLogEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the application log is enabled; otherwise, **False**.

</dd> <dt>

**NodeList**
</dt> <dd> <dl> <dt>

Data type: **NetworkControllerNodeApplicationInfo** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**NetworkControllerNodeApplicationInfo**](networkcontrollernodeapplicationinfo.md)")
</dt> </dl>

Gets a list of [**NetworkControllerNodeApplicationInfo**](networkcontrollernodeapplicationinfo.md) objects containing node specific information.

</dd> <dt>

**RestClientAuthentication**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the REST Client authentication type.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Windows"></span><span id="windows"></span><span id="WINDOWS"></span>

**Windows** ("Windows")


</dt> <dd></dd> <dt>

<span id="x509"></span><span id="X509"></span>

**x509** ("x509")


</dt> <dd></dd> </dl>

</dd> <dt>

**RestClientCertThumbprints**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of thumbprints of the REST Client certificate if the **RestClientAuthentication** is "x509".

</dd> <dt>

**RestClientSecurityGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the security group name to authorize REST Clients in "FQDN\\\\SGName" format if the **RestClientAuthentication** is "Windows".

</dd> <dt>

**RestIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the REST IP address in IP/Prefix format.

</dd> <dt>

**RestURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rest URL as an FQDN.

</dd> <dt>

**SslCertificateRawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

Gets a list of REST SSL certificates.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the version of the Network Controller deployment.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





