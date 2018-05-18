---
Description: 'This reference describes the XML elements that you can use in the XML files or the XML output that represents the results of a stage in a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16504fba-81a5-4977-a58e-1b33f94575ec'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Diagnostic Test Step Result Schema
---

# Diagnostic Test Step Result Schema

This reference describes the XML elements that you can use in the XML files or the XML output that represents the results of a stage in a diagnostic test.

## DiagnosticHelpers.xsd schema file

The following example shows the contents of the DiagnosticHelpers.xsd schema file that defines the XML elements that you can use to specify the results of a stage in a custom diagnostic test.

``` syntax
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="TestResult">
    <xs:complexType>
      <xs:all>
        <xs:element minOccurs="1" maxOccurs="1" name="Name" type="xs:string"/>
        <xs:element minOccurs="1" maxOccurs="1" name="StepResults" nillable="true">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" ref="StepResult"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:all>
    </xs:complexType>
  </xs:element>
  <xs:simpleType name="ResultCode">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NoResult"/>
      <xs:enumeration value="Success"/>
      <xs:enumeration value="Warning"/>
      <xs:enumeration value="Failure"/>
      <xs:enumeration value="Complete"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="ArrayOfNode">
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Node" nillable="true">
        <xs:complexType mixed="true">
          <xs:sequence>
            <xs:element minOccurs="0" ref="Parameters"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="InformationType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Information"/>
      <xs:enumeration value="Failure"/>
      <xs:enumeration value="Warning"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:element name="Parameters" nillable="true">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" maxOccurs="unbounded" name="Parameter" nillable="true">
          <xs:complexType>
            <xs:attribute name="Name" type="xs:string" use="required"/>
            <xs:attribute name="Value" type="xs:string" use="required"/>
            <xs:attribute name="Format" type="xs:string" use="optional"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="StepResult" nillable="true">
    <xs:complexType>
      <xs:all>
        <xs:element minOccurs="0" name="Result" type="ResultCode"/>
        <xs:element minOccurs="0" maxOccurs="1" name="Message" type="xs:string"/>
        <xs:element minOccurs="0" name="ExceptionMessage" type="xs:string"/>
        <xs:element minOccurs="0" name="Nodes" nillable="true" type="ArrayOfNode"/>
        <xs:element minOccurs="0" name="FailedNodes" nillable="true" type="ArrayOfNode"/>
        <xs:element minOccurs="0" name="Environment" nillable="true">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" name="EnvironmentVariable" nillable="true">
                <xs:complexType>
                  <xs:attribute name="Name" type="xs:string" use="required"/>
                  <xs:attribute name="Value" type="xs:string" use="optional"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" name="Tables" nillable="true">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" name="Table" nillable="true">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="Columns">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element maxOccurs="unbounded" name="Column" nillable="true" type="xs:string"/>
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                    <xs:element name="Rows">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element maxOccurs="unbounded" name="Row" nillable="true">
                            <xs:complexType>
                              <xs:sequence>
                                <xs:element name="Items">
                                  <xs:complexType>
                                    <xs:sequence>
                                      <xs:element maxOccurs="unbounded" name="RowItem" nillable="true" type="xs:string"/>
                                    </xs:sequence>
                                  </xs:complexType>
                                </xs:element>
                              </xs:sequence>
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                  <xs:attribute name="Description" type="xs:string" use="optional"/>
                  <xs:attribute name="Name" type="xs:string" use="required"/>
                  <xs:attribute name="Tags" type="xs:string" use="optional"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" name="BulletPoints" nillable="true">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs="0" maxOccurs="unbounded" name="Information" nillable="true">
                <xs:complexType>
                  <xs:all>
                    <xs:element name="Type" type="InformationType"/>
                    <xs:element name="Message" type="xs:string"/>
                  </xs:all>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs="0" ref="Parameters"/>
      </xs:all>
      <xs:attribute name="NodeName">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:minLength value="1"/>
            <xs:maxLength value="64"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="IsSummary">
        <xs:simpleType>
          <xs:restriction base="xs:string">
            <xs:enumeration value="True"/>
            <xs:enumeration value="False"/>
            <xs:enumeration value="true"/>
            <xs:enumeration value="false"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

## In this section

[Diagnostic Test Step Result Elements](diagnostic-test-step-result-elements.md)

 

 



