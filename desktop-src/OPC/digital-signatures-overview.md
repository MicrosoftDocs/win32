---
title: Digital Signatures Overview
description: This topic describes the basics of using Packaging APIs to interact with package digital signatures, which can be used to confirm that signed package components have not been altered since the signature was generated.
ms.assetid: 'd81f6569-6c95-4bb7-9d1d-51e10701b970'
keywords: ["Packaging APIs,digital signatures", "packaging,digital signatures", "packages,digital signatures", "digital signatures", "signatures", "package components"]
---

# Digital Signatures Overview

This topic describes the basics of using Packaging APIs to interact with package digital signatures, which can be used to confirm that signed package components have not been altered since the signature was generated.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Prerequisites](#prerequisites)
-   [Package Signatures](#package-signatures)
-   [Generating a Signature](#generating-a-signature)
    -   [Packaging Interfaces and Methods Used in Signature Generation](#packaging-interfaces-and-methods-used-in-signature-generation)
    -   [Signature Serialization](#signature-serialization)
-   [Accessing and Modifying a Signature](#accessing-and-modifying-a-signature)
    -   [Packaging Interfaces and Methods Used to Access and Modify a Signature](#packaging-interfaces-and-methods-used-to-access-and-modify-a-signature)
-   [Validating a Signature](#validating-a-signature)
    -   [Packaging Interfaces and Methods Used in Validation](#packaging-interfaces-and-methods-used-in-validation)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

A package digital signature (package signature) can be used to confirm that signed package components have not been altered since the signature was generated.

## Prerequisites

For a table of prerequisites, see [Packaging](packaging.md).

## Package Signatures

Windows 7 enables the use of digital signature Packaging APIs by providing an object that implements the [**IOpcDigitalSignatureManager**](iopcdigitalsignaturemanager.md) interface. An instance of this object can be created by calling the [**IOpcFactory::CreateDigitalSignatureManager**](iopcfactory-createdigitalsignaturemanager.md) method of a Packaging factory. For information about how to create a factory for use with the Packaging APIs, see the [Getting Started with the Packaging API](packaging-api-overview.md).

The following table lists the digital signature information that is represented by interfaces in the Packaging APIs. 

| Signature information                     | Packaging interface                                                                        | Description                                                                                                                        |
|-------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| package signature                         | [**IOpcDigitalSignature**](iopcdigitalsignature.md) interface                             | A signature that is created for a package and composed of representations of the other signature concepts.<br/>              |
| reference to a part                       | [**IOpcSignaturePartReference**](iopcsignaturepartreference.md) interface                 | A reference to a part that has been signed. <br/>                                                                            |
| reference to relationships                | [**IOpcSignatureRelationshipReference**](iopcsignaturerelationshipreference.md) interface | A reference to one or more relationships that have been signed and that are all stored in the same Relationships part. <br/> |
| reference to data in the signature markup | [**IOpcSignatureReference**](iopcsignaturereference.md) interface                         | A reference to application data in the signature markup that has been signed. <br/>                                          |
| object that contains application data     | [**IOpcSignatureCustomObject**](iopcsignaturecustomobject.md) interface                   | An application-specific object that contains application data in the signature markup that may have been signed.<br/>        |
| certificate                               | [CERT\_CONTEXT](http://msdn.microsoft.com/library/aa377189(vs.85).aspx) structure    | An X.509 certificate that can be used in signature generation and validation.<br/>                                           |



 

## Generating a Signature

When a signature is generated, a signature part is created to store the associated signature information. Each item to be signed then has its cryptographic hash value (digest value) computed and stored in the package signature markup along with the encrypted hash value that was computed for the entire signature (signature value). These values are accessed when a package signature is validated.

At any time before a signature is generated, the [**IOpcDigitalSignatureManager::SetSignatureOriginPartName**](iopcdigitalsignaturemanager-setsignatureoriginpartname.md) method can be used to set the part name of the Digital Signature Origin part. Although the Digital Signature Origin part does not contain signature markup, it serves as the starting point for locating all signatures in the package. If a part name is not set with this method, a name will be generated at signing time—unless a Digital Signature Origin part already exists in the package that is being signed.

To generate a signature for signing a package, use the following procedure:

1.  Call [**IOpcDigitalSignatureManager::CreateSigningOptions**](iopcdigitalsignaturemanager-createsigningoptions.md) to get a pointer to an object that implements the [**IOpcSigningOptions**](iopcsigningoptions.md) interface.
2.  Use the [**IOpcSigningOptions**](iopcsigningoptions.md) interface methods to set necessary signature information.

    This must include, but is not exclusive to, calls to the following methods:

    -   [**IOpcSigningOptions::SetDefaultDigestMethod**](iopcsigningoptions-setdefaultdigestmethod.md), to set the default digest method
    -   [**IOpcSigningOptions::SetSignatureMethod**](iopcsigningoptions-setsignaturemethod.md), to set the signature method

3.  After all the signature information that is required has been set, call the [**IOpcDigitalSignatureManager::Sign**](iopcdigitalsignaturemanager-sign.md) method. Pass **Sign** a pointer to the [**IOpcSigningOptions**](iopcsigningoptions.md) interface of the object that contains the signature information.

### Packaging Interfaces and Methods Used in Signature Generation

The key Packaging interfaces and interface methods that are used to generate signatures are listed in the following table.

<table>
<thead>
<tr class="header">
<th>Packaging interfaces and methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IOpcDigitalSignatureManager::Sign</strong>](iopcdigitalsignaturemanager-sign.md) method</td>
<td>Signs the package by creating a signature, using a provided certificate and an [<strong>IOpcSigningOptions</strong>](iopcsigningoptions.md) interface. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpcSigningOptions</strong>](iopcsigningoptions.md) interface</td>
<td>Used to set the signature options and properties that are needed to generate a package signature.<br/></td>
</tr>
<tr class="odd">
<td>Set interfaces<br/> <dl>[<strong>IOpcCertificateSet</strong>](iopccertificateset.md)<br />
[<strong>IOpcRelationshipSelectorSet</strong>](iopcrelationshipselectorset.md)<br />
[<strong>IOpcSignatureCustomObjectSet</strong>](iopcsignaturecustomobjectset.md)<br />
[<strong>IOpcSignaturePartReferenceSet</strong>](iopcsignaturepartreferenceset.md)<br />
[<strong>IOpcSignatureReferenceSet</strong>](iopcsignaturereferenceset.md)<br />
[<strong>IOpcSignatureRelationshipReferenceSet</strong>](iopcsignaturerelationshipreferenceset.md)<br />
</dl></td>
<td>These sets of Packaging signature interface pointers provide methods for the creation and deletion of the Packaging digital signature objects that are used to generate a signature. These interfaces are accessed through the [<strong>IOpcSigningOptions</strong>](iopcsigningoptions.md) interface.<br/></td>
</tr>
</tbody>
</table>



 

### Signature Serialization

When a signature is generated, it is serialized as specialized XML markup (signature markup) that complies with the W3C Recommendation for [XML Signature Syntax and Processing](http://go.microsoft.com/fwlink/p/?linkid=132847) (http://go.microsoft.com/fwlink/p/?linkid=132847) and the signature requirements specified in the *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)*.

The following code is an example of the signature markup for a serialized package signature. This markup has been reproduced, with comments added, from the Digital Signature Example in the *OPC*. It shows a serialized signature that has one signed part, several signed relationships (stored in the same Relationships part), and the signed XML markup of an application-specific **Object** element—the only application-specific **Object** that exists in the signature.


```XML
<!-- All the information for a signature exists within the <Signature> 
element. -->
<Signature Id="SignatureId" xmlns="http://www.w3.org/2000/09/xmldsig#">
   <!-- The <SignedInfo> element contains the canonicalization and
   signature methods applied to markup within the <Signature>
   element. This element also contains references to objects in the 
   signature that have been signed. These references are serialized as
   <Reference> elements contained in the <SignedInfo> element. -->
   <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/
         REC-xml-c14n-20010315"/> 
      <SignatureMethod Algorithm="http://www.w3.org/2000/09/
         xmldsig#dsa-sha1"/> 
      <!-- This <Reference> element references the signed package-specific
      <Object> element in the signature. It contains the information that was
      used to generate, and that is needed to validate, the signature. -->
      <Reference 
         URI="#idPackageObject" 
         Type="http://www.w3.org/2000/09/xmldsig#Object">
         <Transforms>
            <Transform Algorithm="http://www.w3.org/TR/2001/
               REC-xml-c14n-20010315"/>
         </Transforms>
         <DigestMethod Algorithm="http://www.w3.org/2000/09/
            xmldsig#sha1"/> 
         <!-- The <DigestValue> element contains the value that was
         computed when the signature was generated. -->
         <DigestValue>...</DigestValue> 
      </Reference>
      <!-- This <Reference> element references signed XML markup in an 
      application-specific <Object> element. It contains the information that
      was used to generate, and that is needed to validate, the signature. -->
      <Reference 
         URI="#Application" 
         Type="http://www.w3.org/2000/09/xmldsig#Object">
         <Transforms>
            <Transform Algorithm="http://www.w3.org/TR/2001/
               REC-xml-c14n-20010315"/>
         </Transforms>
         <DigestMethod 
            Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>            
         <DigestValue>...</DigestValue> 
      </Reference>
   </SignedInfo>
   <!-- The <SignatureValue> element contains the value that was computed
   when the signature was created. -->
   <SignatureValue>...</SignatureValue>

   <!-- The <KeyInfo> element contains certificate information. -->
   <KeyInfo>
      <X509Data>
         <X509Certificate>...</X509Certificate>
      </X509Data>
   </KeyInfo>

   <!-- This <Object> element contains information about which package
   components were signed with this signature. <Reference> elements
   contained in this <Object> reference specific package components
   that were signed by this signature. -->
   <Object Id="idPackageObject" xmlns:pds="http://schemas.openxmlformats.org
     /package/2006/digital-signature">
      <Manifest>
         <!-- This <Reference> is an example of a reference to a signed part. -->
         <Reference URI="/document.xml?ContentType=application/
            vnd.ms-document+xml">
            <Transforms>
               <Transform Algorithm="http://www.w3.org/TR/2001/
                  REC-xml-c14n-20010315"/>
            </Transforms>
            <DigestMethod Algorithm="http://www.w3.org/2000/09/
               xmldsig#sha1"/> 
            <DigestValue>...</DigestValue> 
         </Reference>
         <!-- This <Reference> is an example of a reference to signed
         relationships, which are all stored in the same Relationships
         part. Signed relationships that are stored in different
         Relationships parts are serialized using a <Reference> for each
         Relationships part storing one or more signed relationships. -->
         <Reference 
            URI="/_rels/document.xml.rels?ContentType=application/
               vnd.ms-package.relationships+xml">
            <Transforms>
               <Transform Algorithm="http://schemas.openxmlformats.org/
                  package/2005/06/RelationshipTransform">
                  <pds:RelationshipReference SourceId="B1"/>
                  <pds:RelationshipReference SourceId="A1"/>
                  <pds:RelationshipReference SourceId="A11"/>
                  <pds:RelationshipsGroupReference SourceType=
                     "http://schemas.custom.com/required-resource"/>
               </Transform>
               <Transform Algorithm="http://www.w3.org/TR/2001/
                  REC-xml-c14n-20010315"/>
            </Transforms>
            <DigestMethod Algorithm="http://www.w3.org/2000/09/
               xmldsig#sha1"/> 
            <DigestValue>...</DigestValue> 
         </Reference>
      </Manifest>
      <SignatureProperties>
         <SignatureProperty Id="idSignatureTime" Target="#SignatureId">
            <pds:SignatureTime>
               <pds:Format>YYYY-MM-DDThh:mmTZD</pds:Format>
               <pds:Value>2003-07-16T19:20+01:00</pds:Value>
            </pds:SignatureTime>
         </SignatureProperty> 
      </SignatureProperties>
   </Object>

   <!-- This application-specific <Object> element contains signed
   XML markup. Application-specific <Object> elements can exist in a
   signature regardless of whether or not they contain markup that has
   been signed. -->
   <Object Id="Application">...</Object>
</Signature>
```



## Accessing and Modifying a Signature

If a signed package has been loaded using Packaging APIs, its signatures can be accessed and modified using the digital signature interfaces of the Packaging APIs.

### Packaging Interfaces and Methods Used to Access and Modify a Signature

The key Packaging interfaces and interface methods that are used to access signatures are shown in the following table.

<table>
<thead>
<tr class="header">
<th>Packaging interfaces and methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IOpcDigitalSignatureManager::GetSignatureEnumerator</strong>](iopcdigitalsignaturemanager-getsignatureenumerator.md) method</td>
<td>Gets an enumerator of [<strong>IOpcDigitalSignature</strong>](iopcdigitalsignature.md) interfaces, which represent the signatures of the package. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpcDigitalSignatureManager::GetSignatureOriginPartName</strong>](iopcdigitalsignaturemanager-getsignatureoriginpartname.md) method</td>
<td>Gets an [<strong>IOpcPartUri</strong>](iopcparturi.md) interface that represents the part name of the Digital Signature Origin part.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOpcDigitalSignatureManager::RemoveSignature</strong>](iopcdigitalsignaturemanager-removesignature.md) method</td>
<td>Removes a specified part from the package. This part stores signature markup.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpcDigitalSignatureManager::ReplaceSignature</strong>](iopcdigitalsignaturemanager-replacesignaturexml.md) method</td>
<td>Replaces the existing signature markup that is stored in a specified part.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOpcDigitalSignature</strong>](iopcdigitalsignature.md) interface</td>
<td>Represents a digital signature of a package.<br/></td>
</tr>
<tr class="even">
<td>Enumerator interfaces<br/> <dl>[<strong>IOpcCertificateEnumerator</strong>](iopccertificateenumerator.md)<br />
[<strong>IOpcDigitalSignatureEnumerator</strong>](iopcdigitalsignatureenumerator.md)<br />
[<strong>IOpcRelationshipSelectorEnumerator</strong>](iopcrelationshipselectorenumerator.md)<br />
[<strong>IOpcSignatureCustomObjectEnumerator</strong>](iopcsignaturecustomobjectenumerator.md)<br />
[<strong>IOpcSignaturePartReferenceEnumerator</strong>](iopcsignaturepartreferenceenumerator.md)<br />
[<strong>IOpcSignatureReferenceEnumerator</strong>](iopcsignaturereferenceenumerator.md)<br />
[<strong>IOpcSignatureRelationshipReferenceEnumerator</strong>](iopcsignaturerelationshipreferenceenumerator.md)<br />
</dl></td>
<td>Read-only enumerators for sets that are used for Packaging digital signature tasks.<br/></td>
</tr>
</tbody>
</table>



 

## Validating a Signature

The validation of a package signature indicates that signed package content has not been altered since the signature was generated.

> \[!Important\]  
> The identity of the signer must be validated by the caller.

 

To validate the package signature the digest and signature values are recomputed and compared against the original values that were stored using signature markup when the package signature was generated. Any difference between the recomputed values and the original, stored values indicates that the original data has changed and that this signature is no longer valid.

To validate a signature using the Packaging APIs, call the [**IOpcDigitalSignatureManager::Validate**](iopcdigitalsignaturemanager-validate.md) method.

### Packaging Interfaces and Methods Used in Validation

The Packaging interface method that is used to validate signatures is shown in the following table.

| Packaging interface method                                                            | Description                                                                |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**IOpcDigitalSignatureManager::Validate**](iopcdigitalsignaturemanager-validate.md) | Validates a package signature by using a specified certificate.<br/> |



 

## Additional Resources

While not required to use the Packaging Digital Signature APIs, knowledge of the following security-related technologies will help you understand and use Packaging Digital Signature APIs in your application.



| Technology                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cryptography API](https://msdn.microsoft.com/library/windows/desktop/aa380255)                                              | If your application interacts with package signatures, familiarity with the [Cryptography API](https://msdn.microsoft.com/library/windows/desktop/aa380255)will be helpful. Return codes from Cryptography APIs, especially those related to XML processing, may be returned by some Packaging API methods. For more information, see Cryptography API.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| [XML Signature Syntax and Processing](http://go.microsoft.com/fwlink/p/?linkid=132847) | If your application interacts with package signatures, familiarity with the W3C Recommendation for [XML Signature Syntax and Processing](http://go.microsoft.com/fwlink/p/?linkid=132847)will be helpful. Additionally, Packaging Digital Signature interface and method names also frequently correspond to the names of elements and attributes used in digital signature XML markup, which may inform your understanding of the package signature requirements, which are specified in the OPC. For more information, see [XML Signature Syntax and Processing](http://go.microsoft.com/fwlink/p/?linkid=132847) (http://go.microsoft.com/fwlink/p/?linkid=132847).<br/> |
| [Canonical XML](http://go.microsoft.com/fwlink/p/?linkid=125240)                       | If your application manipulates signature markup, familiarity with the W3C Recommendation for [Canonical XML](http://go.microsoft.com/fwlink/p/?linkid=125240)will be helpful. For more information, see [Canonical XML](http://go.microsoft.com/fwlink/p/?linkid=125240) (http://go.microsoft.com/fwlink/p/?linkid=125240).<br/>                                                                                                                                                                                                                                                                                                                                           |
| [X.509 Digital Certification](https://msdn.microsoft.com/library/windows/desktop/aa388452)                    | If your application uses digital certificates, familiarity with X.509 digital certification (the type of digital certificate used in package signatures) will be helpful. For information about X.509 certification, see [X.509 Digital Certification](https://msdn.microsoft.com/library/windows/desktop/aa388452). For a more general introduction to digital certificates, see [Digital Certificates](https://msdn.microsoft.com/library/windows/desktop/aa381975).<br/>                                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[Digital Signatures Fundamentals](digital-signatures.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Digital Signatures How-To Topics](digital-signatures-how-to-topics.md)
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md)
</dt> <dt>

**Reference**
</dt> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

**External**
</dt> <dt>

[ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> </dl>

 

 





