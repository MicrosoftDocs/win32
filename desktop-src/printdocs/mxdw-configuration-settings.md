---
description: The Microsoft XPS Document Writer (MXDW) enables users to create XPS document files by printing from any Windows application.
ms.assetid: 1fa50337-2df7-48d3-a179-0ca5ae3dfda3
title: MXDW Configuration Settings
ms.topic: article
ms.date: 05/31/2018
---

# MXDW Configuration Settings

The Microsoft XPS Document Writer (MXDW) enables users to create XPS document files by printing from any Windows application. Applications developers can control the following output settings of the MXDW using the PrintTicket and PrintCapabilities parts of the [Print Schema](./printschema.md).

## JobInterleaving

The JobInterleaving setting controls the content interleaving order for the XPS Documents. For information about job interleaving, see the [XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf). MXDW supports the following two options for this setting:

-   **Off** - This option disables interleaving so that all data for each content element in the document is contiguous, which improves the efficiency of random access. This option is best for viewing an XPS document.
-   **On** - This option enables interleaving so that data for each content element is broken up and reordered for more efficient sequential processing. This option is best for web download and printing.

The following example is an example of the PrintCapabilities XML that includes the JobInterleaving setting.


```XML
<psf:Feature name="ns0000:JobInterleaving">
   <psf:Property name="psf:SelectionType">
      <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value> 
   </psf:Property>
   <psf:Property name="psk:DisplayName">
      <psf:Value xsi:type="xsd:string">Interleaving</psf:Value> 
   </psf:Property>
   <psf:Option name="ns0000:OFF" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
         <psf:Value xsi:type="xsd:string">Off - Best for viewing</psf:Value> 
      </psf:Property>
   </psf:Option>
   <psf:Option name="ns0000:ON" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
         <psf:Value xsi:type="xsd:string">On - Best for the web/printing</psf:Value> 
      </psf:Property>
   </psf:Option>
</psf:Feature>
```



The PrintTicket XML is similar, except that it specifies a particular option. See the [Print Schema](./printschema.md) for details.

Since JobInterleaving is not one of the [Print Schema Public Keywords](./print-schema-public-keywords.md), you must include a declaration of the namespace (in this case "ns0000" in the **PrintCapabilities** (or **PrintTicket**) tag at the beginning of the PrintCapabilities (or PrintTicket) document, as shown in the following example:


```XML
<psf:PrintCapabilities 
xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework" 
xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="https://www.w3.org/2001/XMLSchema"  
version="1" 
xmlns:ns0000=http://schemas.microsoft.com/windows/2006/06/printing/printschemakeywords/microsoftxpsdocumentwriter>
```



## JobImageType

JobImageType controls the output format of embedded bitmap formats. MXDW supports the following four options for this setting:

-   **JPEGHigh** - This option specifies the JPEG image with a high level of compression. This option produces the smallest file size, but the lowest image quality.
-   **JPEGMed** - This option specifies the JPEG image with a medium level of compression. This option provides the best balance of file size and image quality.
-   **JPEGLow** - This option specifies the JPEG image with a low level of compression. This option produces the least reduction in file size and high image quality.
-   **PNG** - This option specifies the PNG image format with lossless compression. This option produces the largest file size and the highest image quality.

The PrintCapabilities XML of the JobImageType setting appears below:


```XML
<psf:Feature name="ns0000:JobImageType">
   <psf:Property name="psf:SelectionType">
      <psf:Value xsi:type="xsd:QName">psk:PickOne</psf:Value> 
   </psf:Property>
   <psf:Property name="psk:DisplayName">
      <psf:Value xsi:type="xsd:string">Images</psf:Value> 
   </psf:Property>
   <psf:Option name="ns0000:JPEGHigh" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
         <psf:Value xsi:type="xsd:string">JPG - Maximum compression</psf:Value> 
      </psf:Property>
   </psf:Option>
   <psf:Option name="ns0000:JPEGMed" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
        <psf:Value xsi:type="xsd:string">JPG - Medium compression</psf:Value> 
      </psf:Property>
   </psf:Option>
   <psf:Option name="ns0000:JPEGLow" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
         <psf:Value xsi:type="xsd:string">JPG - Minimum compression</psf:Value> 
      </psf:Property>
   </psf:Option>
   <psf:Option name="ns0000:PNG" constrained="psk:None">
      <psf:Property name="psk:DisplayName">
         <psf:Value xsi:type="xsd:string">PNG - Lossless compression</psf:Value> 
      </psf:Property>
   </psf:Option>
</psf:Feature>
```



The PrintTicket XML is similar, except that it specifies a particular option. See the [Print Schema](./printschema.md) for details.

Since JobImageType is not one of the [Print Schema Public Keywords](./print-schema-public-keywords.md), you must include a declaration of the namespace (in this case "ns0000" in the **PrintCapabilities** (or **PrintTicket**) tag at the beginning of the PrintCapabilities (or PrintTicket) document, as shown in the following example:


```XML
<psf:PrintTicket 
xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework" 
xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="https://www.w3.org/2001/XMLSchema"  
version="1" 
xmlns:ns0000=http://schemas.microsoft.com/windows/2006/06/printing/printschemakeywords/microsoftxpsdocumentwriter>
```



## Related topics

<dl> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> <dt>

[Print Schema](./printschema.md)
</dt> <dt>

[XPS Specification and License Downloads](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 
