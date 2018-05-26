---
title: Report Schema
ms.assetid: 65743ba7-5098-4f8a-88db-530c966bde07
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Report Schema

The Report schema defines the following elements and types that WTP uses to write the contents of a troubleshooting results report:

-   [Report Elements](report-elements.md)
-   [Report Complex Types](report-complex-types.md)

For more information on results reports, see [Reporting](reporting.md).

## The report schema

The following is the report schema that you can use to write transforms for consuming the contents of a results report (an example results report follows the report schema).

``` syntax
<xsd:schema xmlns:dcmRR="http://www.microsoft.com/schemas/dcm/resultreport/2008" 
            xmlns:xsd='http://www.w3.org/2001/XMLSchema' 
            targetNamespace="http://www.microsoft.com/schemas/dcm/resultreport/2008" 
            elementFormDefault="unqualified">

 <xsd:complexType name='ComputerInformation'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='3' maxOccurs='3'/>
  </xsd:sequence>
  <xsd:attribute name='name' type='xsd:string' use='required'/>
 </xsd:complexType>
  
 <xsd:complexType name='PackageInformation'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='3' maxOccurs='3'/>
  </xsd:sequence>
  <xsd:attribute name='id' type='xsd:string' use='required'/>
  <xsd:attribute name='name' type='xsd:string' use='required'/>
 </xsd:complexType>

 <xsd:complexType name='Header'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='2' maxOccurs='2'/>
   <xsd:element name='ComputerInformation' type='dcmRR:ComputerInformation' minOccurs='1' maxOccurs='1'/>
   <xsd:element name='PackageInformation' type='dcmRR:PackageInformation' minOccurs='1' maxOccurs='unbounded'/>
   <xsd:element name='MetaPackageInformation' type='dcmRR:PackageInformation' minOccurs='1' maxOccurs='1'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='DetectionInformation'>
  <xsd:sequence>
   <xsd:element name='DetailedInformation' type='dcmRR:DetailedInformation' minOccurs='1' maxOccurs='1'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='Data'>
  <xsd:simpleContent>
   <xsd:extension base='xsd:string'>
    <xsd:attribute name='id' type='xsd:string' use='required'/>
    <xsd:attribute name='name' type='xsd:string' use='required'/>
   </xsd:extension>
  </xsd:simpleContent>
 </xsd:complexType>

 <xsd:complexType name="Contents">
   <xsd:sequence>
     <xsd:any minOccurs="0" maxOccurs="unbounded" namespace="##any" processContents="lax"/>
   </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='Detail'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='1' maxOccurs='1'/>
   <xsd:element name='Contents' type='dcmRR:Contents' minOccurs='1' maxOccurs='1'/>   
  </xsd:sequence>
  <xsd:attribute name='id' type='xsd:string' use='required'/>
  <xsd:attribute name='name' type='xsd:string' use='required'/>
  <xsd:attribute name='verbosity' type='xsd:string' use='required'/>  
 </xsd:complexType>
 
 <xsd:complexType name='DetailedInformation'>
  <xsd:sequence>
   <xsd:element name='Detail' type='dcmRR:Detail' minOccurs='0' maxOccurs='unbounded'/>
  </xsd:sequence>
 </xsd:complexType>
 
 <xsd:complexType name='Resolution'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='2' maxOccurs='2'/>
   <xsd:element name='DetailedInformation' type='dcmRR:DetailedInformation' minOccurs='1' maxOccurs='1'/>   
  </xsd:sequence>
  <xsd:attribute name='id' type='xsd:string' use='required'/>
  <xsd:attribute name='name' type='xsd:string' use='required'/>
 </xsd:complexType>

 <xsd:complexType name='ResolutionInformation'>
  <xsd:sequence>
   <xsd:element name='Resolution' type='dcmRR:Resolution' minOccurs='0' maxOccurs='unbounded'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='RootCause'>
  <xsd:sequence>
   <xsd:element name='Data' type='dcmRR:Data' minOccurs='2' maxOccurs='2'/>
   <xsd:element name='ResolutionInformation' type='dcmRR:ResolutionInformation' minOccurs='1' maxOccurs='1'/>   
   <xsd:element name='DetectionInformation' type='dcmRR:DetectionInformation' minOccurs='1' maxOccurs='1'/>    
  </xsd:sequence>
  <xsd:attribute name='id' type='xsd:string' use='required'/>
  <xsd:attribute name='name' type='xsd:string' use='required'/>
 </xsd:complexType>

 <xsd:complexType name='RootCauseInformation'>
  <xsd:sequence>
   <xsd:element name='RootCause' type='dcmRR:RootCause' minOccurs='0' maxOccurs='unbounded'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='Problem'>
  <xsd:sequence>
   <xsd:element name='DetectionInformation' type='dcmRR:DetectionInformation' minOccurs='1' maxOccurs='1'/>
   <xsd:element name='RootCauseInformation' type='dcmRR:RootCauseInformation' minOccurs='1' maxOccurs='1'/>   
  </xsd:sequence>
 </xsd:complexType>
 
 <xsd:complexType name='Package'>
  <xsd:sequence>
   <xsd:element name='Problem' type='dcmRR:Problem' minOccurs='1' maxOccurs='1'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:complexType name='ResultReport'>
  <xsd:sequence>
   <xsd:element name='Header' type='dcmRR:Header' minOccurs='1' maxOccurs='1'/>
   <xsd:element name='Package' type='dcmRR:Package' minOccurs='1' maxOccurs='1'/>  
  </xsd:sequence>
  <xsd:attribute name='SchemaVersion' type='xsd:string' use='required'/>
 </xsd:complexType>

 <xsd:element name='ResultReport' type='dcmRR:ResultReport'/>
 
</xsd:schema>
```

## An example results report


```XML
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/xsl" href="results.xsl"?>
<ResultReport SchemaVersion="1.0">
  <Header>
    <Data id="Time" name="Time">Friday, September 25, 2009 1:04:45 PM</Data>
    <Data id="RunningAsAdmin" name="Running As Admin">false</Data>
    <ComputerInformation name="SCOTTWHI6-R2">
      <Data id="Version" name="Windows Version">6.1</Data>
      <Data id="SKU" name="SKU">Server</Data>
      <Data id="Architecture" name="Architecture">amd64</Data>
    </ComputerInformation>
    <PackageInformation id="NetworkDiagnostics" name="Windows Network Diagnostics">
      <Data id="Version" name="Package Version">1.0</Data>
      <Data id="Publisher" name="Publisher">Microsoft Windows</Data>
      <Data id="Description" name="Description">Detects problems with network connectivity.</Data>
    </PackageInformation>
    <MetaPackageInformation id="NetworkDiagnosticsWeb" name="Internet Connections">
      <Data id="Version" name="Package Version">1.0</Data>
      <Data id="Publisher" name="Publisher">Microsoft Corporation</Data>
      <Data id="Description" name="Description">Connect to the Internet or to a particular website.</Data>
    </MetaPackageInformation>
  </Header>
  <Package>
    <Problem>
      <DetectionInformation>
        <DetailedInformation>
          <Detail id="NDFDebugLog" name="Network Diagnostics Log" verbosity="Informational">
            <Data id="Description" name="Description"></Data>
            <Contents>
              <Data id="FileName" name="File Name">3D9D10D8-D1A4-40F0-A548-6675B1C0AE98.Diagnose.0.etl</Data>
            </Contents>
          </Detail>
          <Detail id="NetworkData" name="Other Networking Configuration and Logs" verbosity="Informational">
            <Data id="Description" name="Description"></Data>
            <Contents>
              <Data id="FileName" name="File Name">NetworkConfiguration.cab</Data>
            </Contents>
          </Detail>
        </DetailedInformation>
      </DetectionInformation>
      <RootCauseInformation>
        <RootCause id="{245A9D66-AE9C-4518-A5B4-655752B0A5BD}" name="&amp;quot;%InterfaceName%&amp;quot; doesn't have a valid IP configuration">
          <Data id="Description" name="Description"></Data>
          <Data id="Status" name="Status">Not Checked</Data>
          <ResolutionInformation>
            <Resolution id="{07d37f7b-fa5e-4443-bda7-ab107b29afb9}" name="Reset the &amp;quot;%InterfaceName%&amp;quot; adapter">
              <Data id="Description" name="Description">This can sometimes resolve an intermittent problem.</Data>
              <Data id="Status" name="Status">Not Run</Data>
              <DetailedInformation/>
            </Resolution>
            <Resolution id="{9513cc1c-4a26-4cb8-bf89-0a82129bd105}" name="Investigate router or broadband modem issues">
              <Data id="Description" name="Description">If you're connected to a hotspot or domain network, contact the network administrator. Otherwise:
    1.  Unplug or turn off the device.
    2.  After all the lights on the device are off, wait at least 10 seconds.
    3.  Turn the device on or plug it back into the power outlet.
To restart a router or modem that has a built-in battery, press and quickly release the Reset button.</Data>
              <Data id="Status" name="Status">Not Run</Data>
              <DetailedInformation/>
            </Resolution>
          </ResolutionInformation>
          <DetectionInformation>
            <DetailedInformation/>
          </DetectionInformation>
        </RootCause>

        . . .

      </RootCauseInformation>
    </Problem>
  </Package>
</ResultReport>
```



 

 




