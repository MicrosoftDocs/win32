---
Description: Beginning with Windows Vista, you use an XML manifest to define the performance counters that your provider provides.
ms.assetid: fa13d13a-f2e2-4732-8bf7-cb0a0f1d4ed7
title: Performance Counters Schema
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counters Schema

Beginning with Windows Vista, you use an XML manifest to define the performance counters that your provider provides. The counters are described in the counters section of an instrumentation manifest (for details on what an instrumentation manifest is, see [EventManifest Schema](https://msdn.microsoft.com/library/windows/desktop/aa384043) and [Writing an Instrumentation Manifest](https://msdn.microsoft.com/library/windows/desktop/dd996930)). This section describes the following elements and types that you use to write the counters section of an instrumentation manifest:

-   [Performance Counters Elements](performance-counters-elements.md)
-   [Performance Counters Simple Types](performance-counters-simple-types.md)
-   [Performance Counters Complex Types](performance-counters-complex-types.md)

Do not use the string table in the manifest to specify strings. Instead, specify the strings as string values of the attribute that you are setting. After you run the [CTRPP](ctrpp.md) tool to generate the .rc file, add the localized strings to the .rc file.

When the manifest is complete, call the [CTRPP](ctrpp.md) tool to generate code for your provider. Complete your provider and then run the LodCtr.exe tool to write the name of the binary file that contains the localized resource strings and resource IDs to the registry. You must have administrator privileges to run LodCtr.exe.

The following example shows how to run the LodCtr.exe tool. For complete details on the LodCtr.exe tool, see [Microsoft TechNet](https://go.microsoft.com/fwlink/p/?linkid=84000).

**LodCtr.exe** \[**/m:***manifest* \[*path*\]\]

If you want to update a counter set, run the UnlodCtr.exe tool as shown in the following command-line example. You must pass the same manifest you passed when registering the counter set. After the counter set is unregistered, you can pass the updated manifest to the LodCtr.exe tool.

**UnlodCtr.exe** \[**/m:***manifest*\]

## Performance Counters Schema

The following is the performance counters schema that you can use to validate the counters section of your manifest. Following the schema is an example manifest. For details on the schema that you use to validate the instrumentation section of the manifest, see [EventManifest Schema](https://msdn.microsoft.com/library/windows/desktop/aa384043).

``` syntax
<xs:schema
  targetNamespace="https://schemas.microsoft.com/win/2005/12/counters"
  elementFormDefault="qualified"
  xmlns:man="https://schemas.microsoft.com/win/2005/12/counters"
  xmlns:xs="https://www.w3.org/2001/XMLSchema">

  <xs:simpleType name="GUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value="\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="HexInt32Type">
    <xs:annotation>
      <xs:documentation>Hex 1-8 digits in size</xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:string">
      <xs:pattern value="0[xX][0-9A-Fa-f]{1,8}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="UInt32Type">
    <xs:annotation>
      <xs:documentation>Hex 1-8 digits in size or unsignedInt</xs:documentation>
    </xs:annotation>
    <xs:union memberTypes="xs:unsignedInt man:HexInt32Type"/>
  </xs:simpleType>

  <xs:simpleType name="CSymbolType">
    <xs:annotation>
      <xs:documentation>A Valid C Symbol or an empty string</xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:string">
      <xs:pattern value="()|([_a-zA-Z][_0-9a-zA-Z]*)"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="struct">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="name" type="man:CSymbolType" use="required"/>
        <xs:attribute name="type" type="man:CSymbolType" use="required"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="structs">
    <xs:choice minOccurs="1" maxOccurs="unbounded">
      <xs:element name="struct" type="man:struct"/>
    </xs:choice>
  </xs:complexType>
  
  <xs:complexType name="counterAttribute">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="name" use="required">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:enumeration value="reference"/>
              <xs:enumeration value="noDisplay"/>
              <xs:enumeration value="noDigitGrouping"/>
              <xs:enumeration value="displayAsHex"/>
              <xs:enumeration value="displayAsReal"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:attribute>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  
  <xs:complexType name="counterAttributes">
    <xs:choice minOccurs="1" maxOccurs="5">
      <xs:element name="counterAttribute" type="man:counterAttribute"/>
    </xs:choice>
  </xs:complexType>
  
  <xs:complexType name="counter">
    <xs:choice minOccurs="0" maxOccurs="1">
      <xs:element name="counterAttributes" type="man:counterAttributes">
        <xs:key name="uniqueCounterAttributeName">
          <xs:annotation>
            <xs:documentation>
              Only five counterAttribute elements allowed, they should all be unique.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counterAttribute"/>
          <xs:field xpath="@name"/>
        </xs:key>
      </xs:element>
    </xs:choice>
    <xs:attribute name="symbol" type="man:CSymbolType" use="optional"/>
    <xs:attribute name="id" type="man:UInt32Type" use="required"/>
    <xs:attribute name="uri" type="xs:anyURI" use="required"/>
    <xs:attribute name="name" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:maxLength value="1023"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="description" type="xs:string" use="optional"/>
    <xs:attribute name="type" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="perf_counter_counter"/>
          <xs:enumeration value="perf_counter_timer"/>
          <xs:enumeration value="perf_counter_queuelen_type"/>
          <xs:enumeration value="perf_counter_large_queuelen_type"/>
          <xs:enumeration value="perf_counter_100ns_queuelen_type"/>
          <xs:enumeration value="perf_counter_obj_time_queuelen_type"/>
          <xs:enumeration value="perf_counter_bulk_count"/>
          <xs:enumeration value="perf_counter_text"/>
          <xs:enumeration value="perf_counter_rawcount"/>
          <xs:enumeration value="perf_counter_large_rawcount"/>
          <xs:enumeration value="perf_counter_rawcount_hex"/>
          <xs:enumeration value="perf_counter_large_rawcount_hex"/>
          <xs:enumeration value="perf_sample_fraction"/>
          <xs:enumeration value="perf_sample_counter"/>
          <xs:enumeration value="perf_counter_timer_inv"/>
          <xs:enumeration value="perf_sample_base"/>
          <xs:enumeration value="perf_average_timer"/>
          <xs:enumeration value="perf_average_base"/>
          <xs:enumeration value="perf_average_bulk"/>
          <xs:enumeration value="perf_obj_time_timer"/>
          <xs:enumeration value="perf_100nsec_timer"/>
          <xs:enumeration value="perf_100nsec_timer_inv"/>
          <xs:enumeration value="perf_counter_multi_timer"/>
          <xs:enumeration value="perf_counter_multi_timer_inv"/>
          <xs:enumeration value="perf_counter_multi_base"/>
          <xs:enumeration value="perf_100nsec_multi_timer"/>
          <xs:enumeration value="perf_100nsec_multi_timer_inv"/>
          <xs:enumeration value="perf_raw_fraction"/>
          <xs:enumeration value="perf_large_raw_fraction"/>
          <xs:enumeration value="perf_raw_base"/>
          <xs:enumeration value="perf_large_raw_base"/>
          <xs:enumeration value="perf_elapsed_time"/>
          <xs:enumeration value="perf_counter_delta"/>
          <xs:enumeration value="perf_counter_large_delta"/>
          <xs:enumeration value="perf_precision_system_timer"/>
          <xs:enumeration value="perf_precision_100ns_timer"/>
          <xs:enumeration value="perf_precision_object_timer"/>
          <xs:enumeration value="perf_counter_composite"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="baseID" type="man:UInt32Type" use="optional"/>
    <xs:attribute name="detailLevel" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="standard"/>
          <xs:enumeration value="advanced"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="defaultScale" use="optional" default="0">
      <xs:simpleType>
        <xs:restriction base="xs:integer">
          <xs:minInclusive value="-10"/>
          <xs:maxInclusive value="10"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="aggregate" use="optional">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="sum"/>
          <xs:enumeration value="avg"/>
          <xs:enumeration value="max"/>
          <xs:enumeration value="min"/>
          <xs:enumeration value="undefined"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="perfTimeID" type="man:UInt32Type" use="optional"/>
    <xs:attribute name="perfFreqID" type="man:UInt32Type" use="optional"/>
    <xs:attribute name="multiCounterID" type="man:UInt32Type" use="optional"/>
    <xs:attribute name="struct" type="man:CSymbolType" use="optional">
      <xs:annotation>
        <xs:documentation>
          If providerType=userMode, not allowed.
          If providerType=kernelMode, required.
        </xs:documentation>
      </xs:annotation>
    </xs:attribute>
    <xs:attribute name="field" type="man:CSymbolType" use="optional">
      <xs:annotation>
        <xs:documentation>
          If providerType=userMode, not allowed.
          If providerType=kernelMode, required.
        </xs:documentation>
      </xs:annotation>
    </xs:attribute>
  </xs:complexType>

  <xs:complexType name="counterSet">
    <xs:sequence>
      <xs:element name="structs" type="man:structs" minOccurs="0" maxOccurs="1">
        <xs:annotation>
          <xs:documentation>
            If providerType=userMode, not allowed.
            If providerType=kernelMode, required.
          </xs:documentation>
        </xs:annotation>
      </xs:element>
      <xs:element name="counter" type="man:counter" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="symbol" type="man:CSymbolType" use="required"/>
    <xs:attribute name="guid" type="man:GUIDType" use="required"/>
    <xs:attribute name="uri" type="xs:anyURI" use="required"/>
    <xs:attribute name="name" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:maxLength value="1023"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="description" use="required"/>
    <xs:attribute name="instances" use="optional" default="single">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="single"/>
          <xs:enumeration value="multiple"/>
          <xs:enumeration value="globalAggregate"/>
          <xs:enumeration value="multipleAggregate"/>
          <xs:enumeration value="globalAggregateHistory"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
  
  <xs:complexType name="provider">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <xs:element name="counterSet" type="man:counterSet">
        <xs:key name="uniqueCounterID">
          <xs:annotation>
            <xs:documentation>
              Counter Id should be unique within the counter set.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@id"/>
        </xs:key>
        <xs:unique name="uniqueCounterName">
          <xs:annotation>
            <xs:documentation>
              Counter Name must be unique within the Counter Set. The name is
              case-sensitive.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@name"/>
        </xs:unique>
        <xs:keyref name="existBaseID" refer="man:uniqueCounterID">
          <xs:annotation>
            <xs:documentation>
              A counter with this ID must exist within the same counter set.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@baseID"/>
        </xs:keyref>
        <xs:keyref name="existPerfTimeID" refer="man:uniqueCounterID">
          <xs:annotation>
            <xs:documentation>
              A counter with this ID must exist within the same counter set.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@perfTimeID"/>
        </xs:keyref>
        <xs:keyref name="existPerfFreqID" refer="man:uniqueCounterID">
          <xs:annotation>
            <xs:documentation>
              A counter with this ID must exist within the same counter set.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@perfFreqID"/>
        </xs:keyref>
        <xs:keyref name="existMultiCounterID" refer="man:uniqueCounterID">
          <xs:annotation>
            <xs:documentation>
              A counter with this ID must exist within the same counter set.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@multiCounterID"/>
        </xs:keyref>
        <xs:key name="uniqueStructNames">
          <xs:annotation>
            <xs:documentation>
              Because struct names map to function parameters in generated code,
              the names should be unique.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:structs/man:struct"/>
          <xs:field xpath="@name"/>
        </xs:key>
        <xs:keyref name="existCounterName" refer="man:uniqueStructNames">
          <xs:annotation>
            <xs:documentation>
              Counter name must exist.
            </xs:documentation>
          </xs:annotation>
          <xs:selector xpath="./man:counter"/>
          <xs:field xpath="@struct"/>
        </xs:keyref>
      </xs:element>
    </xs:choice>
    <xs:attribute name="symbol" type="man:CSymbolType" use="optional">
      <xs:annotation>
        <xs:documentation>
          Provider Symbol is required for User Mode providers.
        </xs:documentation>
      </xs:annotation>
    </xs:attribute>
    <xs:attribute name="callback" use="optional" default="default">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="custom"/>
          <xs:enumeration value="default"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="providerGuid" type="man:GUIDType" use="required"/>
    <xs:attribute name="applicationIdentity" type="xs:string" use="required"/>
    <xs:attribute name="providerType" use="optional" default="userMode">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="userMode"/>
          <xs:enumeration value="kernelMode"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="providerName" type="xs:string" use="optional" default="Counters"/>
    <xs:attribute name="resourceBase" type="man:UInt32Type" use="optional"/>
  </xs:complexType>
  
  <xs:complexType name="counters">
    <xs:choice minOccurs="1" maxOccurs="1">
      <xs:element name="provider" type="man:provider"/>
    </xs:choice>
    <xs:attribute name="schemaVersion" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="1.1"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
  
  <xs:element name="counters" type="man:counters">
    <xs:key name="uniqueprovGUID">
      <xs:annotation>
        <xs:documentation>
          Provider GUID should be unique across the entire document.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider"/>
      <xs:field xpath="@providerGuid"/>
    </xs:key>
    <xs:key name="uniqueCounterSetGUID">
      <xs:annotation>
        <xs:documentation>
          Counter Set GUID should be unique across the entire document. The
          counter set registration fails if the GUID is already registered.
          To update a counter set that is registered, you must first
          uninstall the counter set and register it again.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet"/>
      <xs:field xpath="@guid"/>
    </xs:key>
    <xs:key name="uniqueCounterSetURI">
      <xs:annotation>
        <xs:documentation>
          Counter Set URI should be unique across the entire document. The URI
          helps users access the counters in the counter set from any location.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet"/>
      <xs:field xpath="@uri"/>
    </xs:key>
    <xs:key name="uniqueCounterSetName">
      <xs:annotation>
        <xs:documentation>
          Counter Set Name should be unique across the entire document. The
          name is case-sensitive.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet"/>
      <xs:field xpath="@name"/>
    </xs:key>
    <xs:key name="uniqueCounterSetSymbol">
      <xs:annotation>
        <xs:documentation>
          Counter Set Symbol should be unique across the entire document. The
          Symbol is case-sensitive.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet"/>
      <xs:field xpath="@symbol"/>
    </xs:key>
    <xs:unique name="uniqueCounterSymbol">
      <xs:annotation>
        <xs:documentation>
          Counter Symbol should be unique across the entire document. The
          Symbol is case-sensitive.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet/man:counter"/>
      <xs:field xpath="@symbol"/>
    </xs:unique>
    <xs:key name="uniqueCounterURI">
      <xs:annotation>
        <xs:documentation>
          Counter URI must be unique across the entire document. This lets
          users retrieve the counter values from any location.
        </xs:documentation>
      </xs:annotation>
      <xs:selector xpath="./man:provider/man:counterSet/man:counter"/>
      <xs:field xpath="@uri"/>
    </xs:key>
  </xs:element>
  
</xs:schema>
```

## An Example Performance Counters Manifest

The following shows an example manifest that defines performance counters.


```XML
<!-- <?xml version="1.0" encoding="UTF-16"?> -->
<instrumentationManifest     
    xmlns="https://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="https://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="https://www.w3.org/2001/XMLSchema"    
    >

    <instrumentation>

        <counters xmlns="https://schemas.microsoft.com/win/2005/12/counters">

            <provider callback = "custom"
              applicationIdentity = "myprovider.exe"
              providerType = "userMode"
              providerGuid = "{ab8e1320-965a-4cf9-9c07-fe25378c2a23}">

                <counterSet guid = "{dd36a036-c923-4794-b696-70577630b5cf}"
                  uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet1"
                  name = "My LogicalDisk" 
                  description = "This is a sample counter set with multiple instances." 
                  instances = "multiple">

                    <counter id = "1"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet1.MyCounter1"
                      name = "My Free Megabytes"
                      description = "First sample counter."
                      type = "perf_counter_rawcount"
                      detailLevel = "standard"
                      defaultScale = "1"/>

                    <counter id = "2"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet1.MyCounter2"
                      name = "My Avg. Disk sec/Transfer" 
                      description = "Second sample counter." 
                      type = "perf_average_timer"
                      baseID = "3"
                      detailLevel = "advanced"
                      defaultScale = "1">
                      <counterAttributes>
                          <counterAttribute name = "reference" />
                          <counterAttribute name = "displayAsReal" />
                      </counterAttributes>
                    </counter>

                    <counter id = "3"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet1.MyCounter3"
                      type = "perf_average_base"
                      detailLevel = "advanced">
                      <counterAttributes>
                          <counterAttribute name = "noDisplay" />
                      </counterAttributes>
                    </counter>

                </counterSet>

                <counterSet guid = "{f72fdf55-eaa6-45ba-bf6d-4c7cb0d6ef73}"
                  uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2"
                  name = "My System Objects"
                  description = "My System Objects Help."
                  instances = "single">

                    <counter id = "1"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2.MyCounter1"
                      name = "Process Count"
                      description = "Process Count Help."
                      type = "perf_counter_rawcount"
                      detailLevel = "standard"
                      defaultScale = "1">
                      <counterAttributes>
                          <counterAttribute name = "noDigitGrouping" />
                          <counterAttribute name = "displayAsHex" />
                      </counterAttributes>
                    </counter>

                    <counter id = "2"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2.MyCounter2"
                      name = "Thread Count)"
                      description = "Thread Count Help."
                      type = "perf_counter_rawcount">
                    </counter>
 
                    <counter id = "3"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2.MyCounter3"
                      name = "System Elapsed Time"
                      description = "System Elapsed Time Help."
                      type = "perf_elapsed_time"
                      detailLevel = "advanced"
                      perfTimeID = "4"
                      perfFreqID = "5"
                      defaultScale = "1">
                    </counter>

                    <counter id = "4"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2.MyCounter4"
                      type = "perf_counter_large_rawcount">
                      <counterAttributes>
                          <counterAttribute name = "noDisplay" />
                      </counterAttributes>
                    </counter>

                    <counter id = "5"
                      uri = "Microsoft.Windows.System.PerfCounters.MyCounterSet2.MyCounter5"
                      type = "perf_counter_large_rawcount">
                      <counterAttributes>
                          <counterAttribute name = "noDisplay" />
                      </counterAttributes>
                    </counter>

                </counterSet>

            </provider>

        </counters>

    </instrumentation>

</instrumentationManifest>
```



 

 



