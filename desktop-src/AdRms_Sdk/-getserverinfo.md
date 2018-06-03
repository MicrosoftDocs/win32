---
Description: Retrieves an XmlNode object that contains information about an AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b867fb68-d49c-4dd2-80bf-60ef22094171
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: GetServerInfo method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetServerInfo method

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The **GetServerInfo** method retrieves an [XmlNode](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx) object that contains information about an AD RMS server.

> [!Note]  
> This SOAP web method is documented as if it were used in a .NET Framework XML web service client. For information about creating an XML web service client, see [Building XML Web Service Clients](http://go.microsoft.com/fwlink/p/?linkid=87263) and [Accessing XML Web Services in Managed Code](http://go.microsoft.com/fwlink/p/?linkid=87266).

 

## Syntax


```CSharp
public XmlNode[] GetServerInfo(
  ServerInfoRequest[] requests
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public Function GetServerInfo( _
  ByVal requests() As ServerInfoRequest _
) As XmlNode()</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*requests* 
</dt> <dd>

An array of [**ServerInfoRequest**](-serverinforequest.md) objects that specify the type of server information to be retrieved. Each **ServerInfoRequest** object contains a **Type** property that you can use to specify the information to return. The **Type** property contains one of the following values of the [**ServerInfoType**](-serverinfotype.md) enumeration.

<dt>

<span id="VersionInfo"></span><span id="versioninfo"></span><span id="VERSIONINFO"></span>

<span id="VersionInfo"></span><span id="versioninfo"></span><span id="VERSIONINFO"></span>**VersionInfo** ()


</dt> <dd>

Retrieves information about the server version.

</dd> <dt>

<span id="ServerFeatureInfo"></span><span id="serverfeatureinfo"></span><span id="SERVERFEATUREINFO"></span>

<span id="ServerFeatureInfo"></span><span id="serverfeatureinfo"></span><span id="SERVERFEATUREINFO"></span>**ServerFeatureInfo** ()


</dt> <dd>

Retrieves the features supported by the server.

</dd> <dt>

<span id="ServerLicensorCertificate"></span><span id="serverlicensorcertificate"></span><span id="SERVERLICENSORCERTIFICATE"></span>

<span id="ServerLicensorCertificate"></span><span id="serverlicensorcertificate"></span><span id="SERVERLICENSORCERTIFICATE"></span>**ServerLicensorCertificate** ()


</dt> <dd>

Retrieves the server licensor certificate.

</dd> <dt>

<span id="ServiceLocations"></span><span id="servicelocations"></span><span id="SERVICELOCATIONS"></span>

<span id="ServiceLocations"></span><span id="servicelocations"></span><span id="SERVICELOCATIONS"></span>**ServiceLocations** ()


</dt> <dd>

Retrieves the known service location for the server.

</dd> </dl> </dd> </dl>

## Return value

An array of [XmlNode](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx) objects that contain the server information.

## Web Service URL

*ServerURL*/\_wmcs/licensing/server.asmx

*ServerURL*/\_wmcs/certification/server.asmx

## Remarks

The actual structure of the SOAP type varies from language to language. To obtain the structure of the type, query the web service description page.

This method returns all requested information in a single server round trip.

## Examples

The following example shows the XML returned in the [XmlNode](https://msdn.microsoft.com/library/system.xml.xmlnode.aspx) object when all of the types identified by the [**ServerInfoType**](-serverinfotype.md) enumeration are requested.


```XML
<Results xmlns="">
  <ServerInfoRequest Type="VersionInfo" AdditionalInfo="">
    <VersionInfo Version="6.0.0.0"/>
  </ServerInfoRequest>
    
  <ServerInfoRequest Type="ServerFeatureInfo" AdditionalInfo="">
    <ServerFeatureInfo>
      <Feature Name="GroupExpansionWebService" Value="true"/>
      <Feature Name="ActiveDirectoryServicesRemoting" 
               Value="false"/>
      <Feature Name="FederatedServicesEnabled" Value="0"/>
    </ServerFeatureInfo>
  </ServerInfoRequest>
    
  <ServerInfoRequest Type="ServerLicensorCertificate" 
                     AdditionalInfo="">
    <ServerLicensorCertificateChain>
      <!-- This is the same set of XmlNodes that -->
      <!-- GetServerLicensorCertificate returns. -->
        <XrML xmlns="" version="1.2">
              ...

        </XrML>
        <XrML xmlns="" version="1.2">
              ...

        </XrML>
      </ServerLicensorCertificateChain>
  </ServerInfoRequest>
    
  <ServerInfoRequest Type="ServiceLocations" AdditionalInfo="">
    <ServiceLocations>
      <ServiceLocation Type="LicensingService" 
           Url=""/>
      <ServiceLocation Type="PublishingService" 
           Url=""/>
      <ServiceLocation Type="CertificationService" 
           Url="http://localhost/_wmcs/certification/"/>
      <ServiceLocation Type="ActivationService" 
           Url="http://localhost/_wmcs/certification/"/>
      <ServiceLocation Type="PrecertificationService" 
           Url=""/>
      <ServiceLocation Type="ServerService" 
           Url=""/>
      <ServiceLocation Type="GroupExpansionService"
           Url="HTTP://localhost/_wmcs/GroupExpansion/
           GroupExpansion.asmx"/>
    </ServiceLocations>
  </ServerInfoRequest>

</Results>
```



## Requirements



|                                     |                                               |
|-------------------------------------|-----------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                |
| Product<br/>                  | Rights Management Services 1.0 SP2<br/> |



## See also

<dl> <dt>

[AD RMS SOAP Web Methods](ad-rms-soap-web-methods.md)
</dt> <dt>

[**ServerInfoType**](-serverinfotype.md)
</dt> </dl>

 

 




