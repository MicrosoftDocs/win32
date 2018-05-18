---
Description: 'In Windows&\#160;HPC&\#160;Server&\#160;2008&\#160;R2, you can create custom diagnostic tests. You define custom diagnostic tests in an XML file. This reference describes the XML elements that you can use in the content of such files.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a716f2ff-f8ff-42d5-ac7a-cc1f246634bd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Diagnostic Test Definition Schema
---

# Diagnostic Test Definition Schema

In Windows HPC Server 2008 R2, you can create custom diagnostic tests. You define custom diagnostic tests in an XML file. This reference describes the XML elements that you can use in the content of such files.

## DiagnosticTests.xsd schema file

The following example shows the content of the DiagnosticTests.xsd schema file that defines the XML elements that you can use to create a definition for a custom diagnostic test.

``` syntax
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns="" id="DiagnosticTests" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Parameters">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="1" maxOccurs="unbounded" name="Parameter">
          <xs:complexType>
            <xs:attribute name="Name" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:minLength value="1"/>
                  <xs:maxLength value="64"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Value" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="255"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Format" use="optional">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="64"/>
                  <xs:minLength value="1"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="EnvironmentVariables">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="1" maxOccurs="unbounded" name="Variable">
          <xs:complexType>
            <xs:attribute name="Name" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:minLength value="1"/>
                  <xs:maxLength value="255"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Value" use="optional">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="255"/>
                  <xs:minLength value="0"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element msdata:IsDataSet="true" msdata:UseCurrentLocale="true" name="DiagnosticTests">
    <xs:complexType>
      <xs:choice minOccurs="1" maxOccurs="unbounded">
        <xs:element name="DiagnosticTest">
          <xs:complexType>
            <xs:all>
              <xs:element minOccurs="0" maxOccurs="1" name="Parameters">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element minOccurs="1" maxOccurs="unbounded" name="Parameter">
                      <xs:complexType>
                        <xs:attribute name="Name" use="required">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:minLength value="1"/>
                              <xs:maxLength value="64"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="SwitchName" use="optional">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:minLength value="1"/>
                              <xs:maxLength value="64"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="Description" use="optional">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:maxLength value="255"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="Type" use="required">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:enumeration value="Integer"/>
                              <xs:enumeration value="String"/>
                              <xs:enumeration value="Boolean"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="DefaultValue" use="required">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:maxLength value="255"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="MinimumValue" type="xs:long" use="optional"/>
                        <xs:attribute name="MaximumValue" type="xs:long" use="optional"/>
                        <xs:attribute name="Visibility" use="optional">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:enumeration value="True"/>
                              <xs:enumeration value="False"/>
                              <xs:enumeration value="true"/>
                              <xs:enumeration value="false"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="UseOnlyInStep" type="xs:string" use="optional"/>
                        <xs:attribute name="AllowedValues" use="optional">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:maxLength value="2000"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                        <xs:attribute name="Format" use="optional">
                          <xs:simpleType>
                            <xs:restriction base="xs:string">
                              <xs:maxLength value="64"/>
                              <xs:minLength value="1"/>
                            </xs:restriction>
                          </xs:simpleType>
                        </xs:attribute>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
              <xs:element minOccurs="0" maxOccurs="1" ref="EnvironmentVariables"/>
              <xs:element minOccurs="0" maxOccurs="1" name="PreStep">
                <xs:complexType>
                  <xs:all>
                    <xs:element minOccurs="0" maxOccurs="1" ref="Parameters"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="EnvironmentVariables"/>
                  </xs:all>
                  <xs:attribute name="Command" use="required">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:minLength value="1"/>
                        <xs:maxLength value="255"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                  <xs:attribute name="ResultXml" use="optional">
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
              <xs:element minOccurs="0" maxOccurs="1" name="RunStep">
                <xs:complexType>
                  <xs:all>
                    <xs:element minOccurs="0" maxOccurs="1" ref="Parameters"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="EnvironmentVariables"/>
                  </xs:all>
                  <xs:attribute name="Command" use="required">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:minLength value="1"/>
                        <xs:maxLength value="255"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                  <xs:attribute name="ResultXml" use="optional">
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
              <xs:element minOccurs="0" maxOccurs="1" name="PostStep">
                <xs:complexType>
                  <xs:all>
                    <xs:element minOccurs="0" maxOccurs="1" ref="Parameters"/>
                    <xs:element minOccurs="0" maxOccurs="1" ref="EnvironmentVariables"/>
                  </xs:all>
                  <xs:attribute name="Command" use="required">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:minLength value="1"/>
                        <xs:maxLength value="255"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                  <xs:attribute name="ResultXml" use="optional">
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
              <xs:element minOccurs="0" maxOccurs="1" name="AutoGenerateResult">
                <xs:complexType>
                  <xs:attribute name="TestType" use="required">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:enumeration value="Consistency"/>
                        <xs:enumeration value="Comparison"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                  <xs:attribute name="ExpectedValue" use="optional">
                    <xs:simpleType>
                      <xs:restriction base="xs:string">
                        <xs:minLength value="1"/>
                        <xs:maxLength value="64"/>
                      </xs:restriction>
                    </xs:simpleType>
                  </xs:attribute>
                </xs:complexType>
              </xs:element>
            </xs:all>
            <xs:attribute name="Name" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:minLength value="1"/>
                  <xs:maxLength value="255"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Alias" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:minLength value="1"/>
                  <xs:maxLength value="64"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Description" use="optional">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="255"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Company" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="128"/>
                  <xs:minLength value="1"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Suite" use="required">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:minLength value="1"/>
                  <xs:maxLength value="128"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="Version" use="optional">
              <xs:simpleType>
                <xs:restriction base="xs:string">
                  <xs:maxLength value="64"/>
                </xs:restriction>
              </xs:simpleType>
            </xs:attribute>
          </xs:complexType>
        </xs:element>
      </xs:choice>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

## In this section

[Diagnostic Test Definition Elements](diagnostic-test-definition-elements.md)

 

 



