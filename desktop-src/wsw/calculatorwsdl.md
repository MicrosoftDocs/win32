---
title: CalculatorWsdl
description: This is an example wsdl/schema for the calculator service samples.
ms.assetid: 6dbea7dc-2d5c-4e6d-9941-9a93943e1914
keywords:
- CalculatorWsdl Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# CalculatorWsdl

This is an example wsdl/schema for the calculator service samples.

## Calculator.wsdl

``` syntax
<wsdl:definitions 
  xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
  xmlns:wsu="https://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" 
  xmlns:soapenc="https://schemas.xmlsoap.org/soap/encoding/" 
  xmlns:tns="https://Example.org" 
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing" 
  xmlns:wsp="https://schemas.xmlsoap.org/ws/2004/09/policy" 
  xmlns:wsap="https://schemas.xmlsoap.org/ws/2004/08/addressing/policy" 
  xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
  xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" 
  xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
  xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
  xmlns:wsa10="https://www.w3.org/2005/08/addressing" 
  xmlns:wsx="https://schemas.xmlsoap.org/ws/2004/09/mex" targetNamespace="https://Example.org" 
  xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <xsd:schema targetNamespace="https://Example.org" elementFormDefault="qualified" >
  <xsd:element name="Add">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element minOccurs="0" name="a" type="xsd:int" />
        <xsd:element minOccurs="0" name="b" type="xsd:int" />
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
  <xsd:element name="AddResponse">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element minOccurs="0" name="result" type="xsd:int" />
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
  <xsd:element name="Subtract">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element minOccurs="0" name="a" type="xsd:int" />
        <xsd:element minOccurs="0" name="b" type="xsd:int" />
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
  <xsd:element name="SubtractResponse">
    <xsd:complexType>
      <xsd:sequence>
        <xsd:element minOccurs="0" name="result" type="xsd:int" />
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>
    </xsd:schema>
  </wsdl:types>
  <wsdl:message name="ICalculator_Add_InputMessage">
    <wsdl:part name="parameters" element="tns:Add" />
  </wsdl:message>
  <wsdl:message name="ICalculator_Add_OutputMessage">
    <wsdl:part name="parameters" element="tns:AddResponse" />
  </wsdl:message>
  <wsdl:message name="ICalculator_Subtract_InputMessage">
    <wsdl:part name="parameters" element="tns:Subtract" />
  </wsdl:message>
  <wsdl:message name="ICalculator_Subtract_OutputMessage">
    <wsdl:part name="parameters" element="tns:SubtractResponse" />
  </wsdl:message>
  <wsdl:portType name="ICalculator">
    <wsdl:operation name="Add">
      <wsdl:input wsaw:Action="https://Example.org/ICalculator/Add" message="tns:ICalculator_Add_InputMessage" />
      <wsdl:output wsaw:Action="https://Example.org/ICalculator/AddResponse" message="tns:ICalculator_Add_OutputMessage" />
    </wsdl:operation>
    <wsdl:operation name="Subtract">
      <wsdl:input wsaw:Action="https://Example.org/ICalculator/Subtract" message="tns:ICalculator_Subtract_InputMessage" />
      <wsdl:output wsaw:Action="https://Example.org/ICalculator/SubtractResponse" message="tns:ICalculator_Subtract_OutputMessage" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="DefaultBinding_ICalculator" type="tns:ICalculator">
    <soap:binding transport="https://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="Add">
      <soap:operation soapAction="https://Example.org/ICalculator/Add" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Subtract">
      <soap:operation soapAction="https://Example.org/ICalculator/Subtract" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="CalculatorService">
        <wsdl:port name="ICalculator" binding="tns:DefaultBinding_ICalculator">
            <soap:address location="https://Example.org/ICalculator" />
        </wsdl:port> 
  </wsdl:service>
</wsdl:definitions>
```

 

 




