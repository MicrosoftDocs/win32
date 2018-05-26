---
title: Differences between the Native and Managed APIs
description: This topic describes the programming differences between the native-code Packaging API, introduced in Windows 7, and its managed-code System.IO.Packaging API counterpart.
ms.assetid: a1a6c3ea-c143-4e0c-982a-f7c6b5d16ec8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Differences between the Native and Managed APIs

This topic describes the programming differences between the native-code Packaging API, introduced in Windows 7, and its managed-code [**System.IO.Packaging API**](frlrfSystemIOPackaging) counterpart.

This topic contains the following sections:

-   [Introduction](#introduction)
-   [Who is Affected by the API Differences](#who-is-affected-by-the-api-differences)
-   [Comparing the Native Packaging API to its Managed Counterpart](#comparing-the-native-packaging-api-to-its-managed-counterpart)
    -   [Pack URI Comparison](#pack-uri-comparison)
-   [Related topics](#related-topics)

## Introduction

The description of the programming differences between the native Packaging API and its managed [**System.IO.Packaging API**](frlrfSystemIOPackaging) counterpart that appears in this topic originally appeared as two Packaging Team blog posts: [Comparing the OPC Managed-Code and Native-Code APIs](http://blogs.msdn.com/opc/archive/2009/08/05/comparison-between-the-opc-managed-code-and-native-code-apis.aspx), posted August 5th, 2009; and [Comparing the OPC managed-code and native-code Part URI helper APIs](http://blogs.msdn.com/opc/archive/2009/08/18/comparing-the-opc-managed-code-and-native-code-part-uri-helper-apis.aspx), posted August 18th, 2009.

## Who is Affected by the API Differences

If you are a developer who wants to transition your application to or from a native-code environment, you may need to make changes in your application code to adjust for differences between the two APIs.

The differences described in this topic can help you identify which blocks of application code may need to be reworked as a result of a code-base transition.

## Comparing the Native Packaging API to its Managed Counterpart

Both the managed [**System.IO.Packaging API**](frlrfSystemIOPackaging) and the native Packaging API were designed to adhere to the ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC). The packages created by one API can be accessed by the other API.

The following table compares the native Packaging API implementation to the managed [**System.IO.Packaging API**](frlrfSystemIOPackaging) implementation for specific API features that have notable differences.



| API Feature                                                       | Native Packaging API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Managed [**System.IO.Packaging API**](frlrfSystemIOPackaging)                                                                                                                                                                                                                                                                                           | Comments                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zip encoding<br/>                                           | Enables you to specify the Zip encoding when calling the [**WritePackageToStream**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-writepackagetostream?branch=master) method of the [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) interface to serialize package.<br/> The default encoding is ZIP64.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        | Determines Zip encoding automatically.<br/> The default encoding is ZIP32. If the package size exceeds ZIP32 limits, ZIP64 encoding is used.<br/>                                                                                                                                                                                           | This difference means that if you use the native Packaging API to specify ZIP32 encoding and your package exceeds ZIP32 size limits, the package will not be serialized and the method will return an error.<br/>                                                                                                                                                   |
| Editing in-place<br/>                                       | No equivalent feature.<br/> Changes must be saved as a new package, which can then be made to replace the original.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Enables saving changes to the original package.<br/>                                                                                                                                                                                                                                                                                              | Editing in-place using the native Packaging API would require opening two streams to package at the same time, or opening one read/write stream to the package, neither of which is supported.<br/>                                                                                                                                                                 |
| Core Properties part interaction<br/>                       | No equivalent feature.<br/> The Core Properties part can be read and edited by using the same procedures used to access any other part in the package.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Provides the [**PackageProperties**](frlrfSystemIOPackagingPackagePropertiesClassTopic) class to enable reading and editing of the Core Properties part.<br/>                                                                                                                                                                                     | The [Set Author Sample](set-author-sample.md) shows how to access and edit Core Properties part content by using the native Packaging API. The procedures used in the Set Author Sample are explained in greater detail in [Finding the Core Properties Part](finding-the-core-properties-part.md) and [Modifying Part Content](modifying-part-content.md).<br/> |
| Pack URI support<br/>                                       | Provides the [**CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master) method of the [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) interface and the [**IOpcUri**](/windows/previous-versions/msopc/nn-msopc-iopcuri?branch=master) and [**IOpcPartUri**](/windows/previous-versions/msopc/nn-msopc-iopcparturi?branch=master) interfaces, to support creating URIs that address parts (part names), the path component of the Pack URI scheme. <br/>                                                                                                                                                                                                                                                                                                                                                                      | Provides the [**PackUriHelper**](frlrfSystemIOPackagingPackUriHelperClassTopic) class to support creating URIs that adhere to the Pack URI scheme and that can address both parts in a package and an entire package.<br/>                                                                                                                        | The Pack URI scheme is specified in Annex B. Pack URI of the OPC.<br/> Because the native Packaging API only make use of part names, the API only support operations with this component of the Pack URI scheme.<br/> For a more detailed comparison of Pack URI support, see [Pack URI Comparison](#pack-uri-comparison).<br/>                         |
| Accessing content within a package stored on a website<br/> | No equivalent feature.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Provides the [**PackWebRequest**](frlrfSystemIOPackagingPackWebRequestClassTopic) and [**PackWebResponse**](frlrfSystemIOPackagingPackWebResponseClassTopic) classes that enable access to content within a URI-addressable package that is stored on a website.<br/>                                                                             | The [**System.IO.Packaging API**](frlrfSystemIOPackaging) classes are based on the managed-code [**WebRequest**](frlrfSystemNetWebRequestClassTopic) and [**WebResponse**](frlrfSystemNetWebResponseClassTopic) classes that support URI requests to access resources over the web.<br/>                                                                            |
| Accessing a package without a Content Types stream<br/>     | The call to the [**ReadPackageFromStream**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-readpackagefromstream?branch=master) method of the [**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master) interface fails and returns an error code.<br/> The native API considers a missing Content Types stream to be an error.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                           | The call to the [**Package.Open**](frlrfSystemIOPackagingPackageClassOpenTopic) method succeeds and the package is opened, but it is treated as an empty package.<br/> Without the Content Types stream, parts in the package are not recognized as valid parts.<br/>                                                                       | The behavior of each API differs when the Content Types stream is missing because the OPC specification is non-specific about how this situation should be handled.<br/>                                                                                                                                                                                            |
| Relationships part compression<br/>                         | Relationships parts use a default compression of **OPC\_COMPRESSION\_NORMAL**, which balances between size and performance concerns.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Relationships parts are compressed with the same compression as the source part; for the package Relationships part, no compression is used.<br/>                                                                                                                                                                                                 | For more information about compression options used in the native Packaging API, see [**OPC\_COMPRESSION\_OPTIONS**](/windows/previous-versions/msopc/ne-msopc-__midl___midl_itf_msopc_0000_0002_0002?branch=master).<br/>                                                                                                                                                                                                             |
| Treatment of Relationships parts<br/>                       | Treats Relationships parts as different from other parts and therefore does not allow direct access to Relationships parts. <br/> For example, if you try to retrieve a Relationships part from the set of normal parts by calling the [**GetPart**](/windows/previous-versions/msopc/nf-msopc-iopcpartset-getpart?branch=master) method of the [**IOpcPartSet**](/windows/previous-versions/msopc/nn-msopc-iopcpartset?branch=master) interface, the method will return an error. Instead, Relationships parts can be accessed by calling the [**GetRelationshipSet**](/windows/previous-versions/msopc/nf-msopc-iopcpart-getrelationshipset?branch=master) method of the [**IOpcPart**](/windows/previous-versions/msopc/nn-msopc-iopcpart?branch=master) interface or the [**GetRelationshipSet**](/windows/previous-versions/msopc/nf-msopc-iopcpackage-getrelationshipset?branch=master) method of the [**IOpcPackage**](/windows/previous-versions/msopc/nn-msopc-iopcpackage?branch=master) interface.<br/> | Treats Relationships parts the same as other parts. All operations that are permitted on parts also work on Relationships parts.<br/> For example, it enables the use of the [**Package.GetPart**](frlrfSystemIOPackagingPackageClassGetPartTopic) method with the part name of a Relationships part to get that part and its content.<br/> | The native Packaging API treats Relationships parts as distinct from other parts because they can behave differently from other parts. For example, a Relationships part cannot be the source of a relationship like a normal part.<br/>                                                                                                                            |
| Accessing the content stream of a Relationships part<br/>   | Provides read-only access to a stream of Relationships part content by calling the [**GetRelationshipsContentStream**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipset-getrelationshipscontentstream?branch=master) method of the [**IOpcRelationshipSet**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipset?branch=master) interface.<br/> To add or delete a relationship in the Relationships part, call the [**CreateRelationship**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipset-createrelationship?branch=master) or [**DeleteRelationship**](/windows/previous-versions/msopc/nf-msopc-iopcrelationshipset-deleterelationship?branch=master) method of the [**IOpcRelationshipSet**](/windows/previous-versions/msopc/nn-msopc-iopcrelationshipset?branch=master) interface, respectively.<br/>                                                                                                             | Provides read/write access to a stream of Relationships part content by calling the [**PackagePart.GetStream**](Overload:System.IO.Packaging.PackagePart.GetStream) method.<br/> The stream can be used to add, delete, or modify the relationships stored in the accessed Relationships part.<br/>                                         | Read access to Relationships part content is provided by the native Packaging API solely for digital signature purposes.<br/>                                                                                                                                                                                                                                       |



 

### Pack URI Comparison

In contrast to the centralized Pack URI support provided by the managed [**System.IO.Packaging API**](frlrfSystemIOPackaging), the native Packaging API provides decentralized Pack URI support with the [**IOpcFactory::CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master) method and the [**IOpcUri**](/windows/previous-versions/msopc/nn-msopc-iopcuri?branch=master) and [**IOpcPartUri**](/windows/previous-versions/msopc/nn-msopc-iopcparturi?branch=master) interfaces.

Unlike the managed [**System.IO.Packaging API**](frlrfSystemIOPackaging), the native Packaging API does not enable access to a package or its content as an external resource, and therefore supports part names to address part content only within the current package.

Despite these differences, both native and managed implementations adhere to the OPC.

The following table shows a detailed comparison of Pack URI support in the native Packaging API and managed [**System.IO.Packaging API**](frlrfSystemIOPackaging).



| Native Packaging API                                                                         | Managed [**System.IO.Packaging API**](frlrfSystemIOPackaging)                                                                                                | Equivalence                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOpcFactory::CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master)<br/>                   | [**PackUriHelper.CreatePartUri**](frlrfSystemIOPackagingPackUriHelperClassCreatePartUriTopic)<br/>                                                     | See [Detailed Comparison of IOpcFactory::CreatePartUri and PackUriHelper.CreatePartUri](#detailed-comparision-of-iopcfactorycreateparturi-and-packurihelpercreateparturi)<br/> |
| [**IOpcFactory::CreatePackageRootUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createpackagerooturi?branch=master)<br/>     | No equivalent API<br/>                                                                                                                                 | None<br/>                                                                                                                                                                      |
| [**IOpcUri::GetRelationshipsPartUri**](/windows/previous-versions/msopc/nf-msopc-iopcuri-getrelationshipsparturi?branch=master)<br/>       | [**PackUriHelper.GetRelationshipPartUri**](frlrfSystemIOPackagingPackUriHelperClassGetRelationshipPartUriTopic)<br/>                                   | Identical<br/>                                                                                                                                                                 |
| [**IOpcUri::GetRelativeUri**](/windows/previous-versions/msopc/nf-msopc-iopcuri-getrelativeuri?branch=master)<br/>                         | [**PackUriHelper.GetRelativeUri**](frlrfSystemIOPackagingPackUriHelperClassGetRelativeUriTopic)<br/>                                                   | Identical<br/>                                                                                                                                                                 |
| [**IOpcUri::CombinePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcuri-combineparturi?branch=master)<br/>                         | [**PackUriHelper.ResolvePartUri**](frlrfSystemIOPackagingPackUriHelperClassResolvePartUriTopic)<br/>                                                   | See [Detailed Comparision of IOpcUri::CombinePartUri and PackUriHelper.ResolvePartUri](#detailed-comparision-of-iopcuricombineparturi-and-packurihelperresolveparturi)<br/>    |
| [**IOpcPartUri::ComparePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcparturi-compareparturi?branch=master)<br/>                 | [**PackUriHelper.ComparePartUri**](frlrfSystemIOPackagingPackUriHelperClassComparePartUriTopic)<br/>                                                   | Identical<br/>                                                                                                                                                                 |
| [**IOpcPartUri::GetSourceUri**](/windows/previous-versions/msopc/nf-msopc-iopcparturi-getsourceuri?branch=master)<br/>                     | [**PackUriHelper.GetSourcePartUriFromRelationshipPartUri**](frlrfSystemIOPackagingPackUriHelperClassGetSourcePartUriFromRelationshipPartUriTopic)<br/> | Identical<br/>                                                                                                                                                                 |
| [**IOpcPartUri::IsRelationshipsPartUri**](/windows/previous-versions/msopc/nf-msopc-iopcparturi-isrelationshipsparturi?branch=master)<br/> | [**PackUriHelper.IsRelationshipPartUri**](frlrfSystemIOPackagingPackUriHelperClassIsRelationshipPartUriTopic)<br/>                                     | Identical<br/>                                                                                                                                                                 |
| No equivalent<br/>                                                                     | [**PackUriHelper.Create**](Overload:System.IO.Packaging.PackUriHelper.Create)<br/>                                                                     | None<br/>                                                                                                                                                                      |
| No equivalent<br/>                                                                     | [**PackUriHelper.ComparePackUri**](frlrfSystemIOPackagingPackUriHelperClassComparePackUriTopic)<br/>                                                   | None<br/>                                                                                                                                                                      |
| No equivalent<br/>                                                                     | [**PackUriHelper.GetNormalizedPartUri**](frlrfSystemIOPackagingPackUriHelperClassGetNormalizedPartUriTopic)<br/>                                       | None<br/>                                                                                                                                                                      |
| No equivalent<br/>                                                                     | [**PackUriHelper.GetPackageUri**](frlrfSystemIOPackagingPackUriHelperClassGetPackageUriTopic)<br/>                                                     | None<br/>                                                                                                                                                                      |
| No equivalent<br/>                                                                     | [**PackUriHelper.GetPartUri**](frlrfSystemIOPackagingPackUriHelperClassGetPartUriTopic)<br/>                                                           | None<br/>                                                                                                                                                                      |



 

### Detailed Comparision of IOpcFactory::CreatePartUri and PackUriHelper.CreatePartUri

Both the native and managed implementations adhere to the OPC requirements for creating part names. While both implementations should also adhere to the requirements of [RFC 3987: Internationalized Resource Identifiers (IRIs)](http://go.microsoft.com/fwlink/p/?linkid=162394), the managed [**PackUriHelper.CreatePartUri**](frlrfSystemIOPackagingPackUriHelperClassCreatePartUriTopic) class method violates those requirements if the input contains bad UTF-encoding.

In addition, the native [**IOpcFactory::CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master) interface method differs from its managed counterpart because the interface method ensures that the part names it returns are valid.

The following table shows these differences by comparing the behavior of the native and managed implementations.



| Input                                                               | Native [**IOpcFactory::CreatePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createparturi?branch=master) Behavior                                             | Managed [**PackUriHelper.CreatePartUri**](frlrfSystemIOPackagingPackUriHelperClassCreatePartUriTopic) Behavior                                                                                                                               |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Begins with more than one forward slash.<br/>                 | Collapses multiple forward slashes to a single forward slash, and returns a valid part name.<br/>                     | Fails and throws an ArgumentException.<br/>                                                                                                                                                                                            |
| Contains empty segments (multiple forward slashes).<br/>      | Collapses empty segments to a single forward slash, and returns a valid part name.<br/>                               | Does not collapse empty segments, and returns an invalid part name.<br/>                                                                                                                                                               |
| Contains bad UTF-8 encoding.<br/> For example: %FC<br/> | Preserves encoding, and returns a valid part name.<br/> For example: %FC would be unchanged in the output.<br/> | Changes to valid UTF-8 encoding, and returns a valid part name.<br/> For example: %FC would be changed to %C3%BC in the output, which violates requirements of [RFC 3987](http://go.microsoft.com/fwlink/p/?linkid=162394).<br/> |
| Contains a percent-encoded **NULL** (%00).<br/>               | Fails and returns an E\_UNEXPECTED error code.<br/>                                                                   | Percent-encoded **NULL** is unchanged, and returns a valid part name.<br/>                                                                                                                                                             |
| Ends with a forward slash.<br/>                               | Removes trailing forward slash, and returns a valid part name.<br/>                                                   | Fails and throws an ArgumentException.<br/>                                                                                                                                                                                            |



 

> [!Note]  
> Characters above 0x7F must be escaped using UTF-8.

 

### Detailed Comparision of IOpcUri::CombinePartUri and PackUriHelper.ResolvePartUri

There are a significant behavioral differences between these native and managed implementations because they adhere to different sets of requirements.

The native [**IOpcUri::CombinePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcuri-combineparturi?branch=master) interface method adheres to the requirements from both [RFC 3987](http://go.microsoft.com/fwlink/p/?linkid=162394) and section A.3 of the OPC. As a result, the part names that are returned by this interface method are valid.

In contrast, the managed [**PackUriHelper.ResolvePartUri**](frlrfSystemIOPackagingPackUriHelperClassResolvePartUriTopic) class method adheres to the requirements from [RFC 3987](http://go.microsoft.com/fwlink/p/?linkid=162394) but not section A.3 of the OPC. As a result, the part names that are returned by this class method may be invalid.

The following table shows these differences by comparing the behavior of the native and managed implementations.



| Input                                                               | Native [**IOpcUri::CombinePartUri**](/windows/previous-versions/msopc/nf-msopc-iopcuri-combineparturi?branch=master) Behavior                                               | Managed [**PackUriHelper.ResolvePartUri**](frlrfSystemIOPackagingPackUriHelperClassResolvePartUriTopic) Behavior                     |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Begins with more than one forward slash.<br/>                 | Collapses multiple forward slashes to a single forward slash, and returns a valid part name.<br/>                 | Fails and throws an ArgumentException, which violates requirements of section A.3 OPC.<br/>                                    |
| Contains empty segments (multiple forward slashes).<br/>      | Collapses empty segments to a single forward slash, and returns a valid part name.<br/>                           | Does not collapse empty segments, which violates requirements of section A.3 OPC, and returns an invalid part name.<br/>       |
| Contains bad UTF-8 encoding.<br/> For example: %FC<br/> | Preserves encoding, and returns a valid part name.<br/> For example: %FC would be unchanged in output.<br/> | Preserves encoding, and returns a valid part name.<br/> For example: %FC would be unchanged in output.<br/>              |
| Contains percent-encoded unreserved characters.<br/>          | Un-encodes unreserved characters, and returns a valid part name.<br/>                                             | Preserves encoding, which violates requirements of section A.3 OPC, and returns an invalid part name.<br/>                     |
| Contains a percent-encoded **NULL** (%00).<br/>               | Fails and returns an E\_UNEXPECTED error code.<br/>                                                               | Percent-encoded **NULL** is unchanged, and returns a valid part name.<br/>                                                     |
| Ends with a forward slash.<br/>                               | Removes trailing forward slash, and returns a valid part name.<br/>                                               | Does not remove trailing forward slash, which violates requirements of section A.3 OPC, and returns an invalid part name.<br/> |



 

## Related topics

<dl> <dt>

[Packaging API Programming Guide](packaging-programming-guide.md)
</dt> <dt>

**Reference**
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md)
</dt> <dt>

**External**
</dt> <dt>

[ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> </dl>

 

 





