---
title: Gadgets for Windows Sidebar Manifest
description: The gadget \ 0034;manifest \ 0034; is an XML file that contains general configuration and presentation information for a gadget.
ms.assetid: '3f26c22f-f48a-44c7-9313-d9766b75c4d9'
keywords: ["Windows Sidebar,manifest", "Sidebar,manifest", "gadgets,manifest", "Gadget.xml", "Windows Sidebar,examples", "Sidebar,examples", "gadgets,examples", "Gadget Picker,manifest", "Windows Sidebar,elements", "Sidebar,elements", "gadgets,elements"]
---

# Gadgets for Windows Sidebar Manifest

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

The gadget "manifest" is an XML file that contains general configuration and presentation information for a gadget. This information is presented to the user through the **Gadget Picker** as gadget and developer details, along with various functional or informational icons. Each gadget package must include a manifest.

> [!Note]  
> The gadget manifest file **must** be named "gadget.xml".

 

-   [Sample Gadget Manifest](#sample-gadget-manifest)
-   [Manifest Elements](#manifest-elements)

## Sample Gadget Manifest

This example shows the data and structure of a valid gadget manifest.


```
<?xml version="1.0" encoding="utf-8" ?>
<gadget>
  <name>Sample Gadget</name>
  <namespace>windows.sdk</namespace>
  <version>1.0.0.0</version>
  <author name="Microsoft">
    <info url="msdn.microsoft.com" />
    <logo src="logo.png" />
  </author>
  <copyright>&amp;#169; Microsoft Corporation.</copyright>
  <description>Sidebar gadget sample.</description>
  <icons>
    <icon height="48" width="48" src="icon.png" />
  </icons>
  <hosts>
    <host name="sidebar">
      <base type="HTML" apiVersion="1.0.0" src="sample.html" />
      <permissions>Full</permissions>
      <platform minPlatformVersion="1.0" />
      <defaultImage src="icon.png" />
    </host>
  </hosts>
</gadget>
```



## Manifest Elements

This section defines the individual elements of a gadget manifest.

![gadget picker with manifest elements highlighted.](images/manifest/gadgetpicker-with-callouts.png)

-   **&lt;xml&gt; Element**

    Required.

    The XML declaration defines the XML version and the character encoding used in the document. This particular document conforms to the 1.0 specification of XML and uses the UTF-8 (Unicode) character set.

    Attributes:

    -   Version. Required. The expected value is 1.0.
    -   Encoding. Required. The expected value is UTF-8.

-   **&lt;gadget&gt; Element**

    Required.

    A container for child elements that describe the gadget. It has no attributes.

    Elements:

    -   **&lt;name&gt; Element**

        Required.

        A user-friendly name that is displayed in the gadget picker, on the Windows Sidebar page of the control panel, and the Sidebar itself.

    -   **&lt;version&gt; Element**

        Required.

        Specifies the version information for the gadget.

        Sidebar uses this value during gadget installation. If another gadget of the same name has already been installed, Sidebar does a version comparison. If the versions differ, the user is prompted to select the appropriate version.

        Valid version strings are of the form major.minor.revision.build. Each of these numbers (or octets) can contain 0 to 4 digits between the values of 0 and 9, inclusive.

    -   **&lt;hosts&gt; Element**

        Required.

        A container for one or more &lt;host&gt; elements. It has no attributes.

        Elements:

        -   **&lt;host&gt; Element**

            Required.

            Identifies the application that hosts the gadget (currently, only "sidebar" is supported). Its child elements define the gadget's behavior for a specific host application.

            Attributes:

            -   Name. Required. The expected value is "sidebar".

            Elements:

            -   **&lt;base&gt; Element**

                Required.

                Provides Sidebar with a gadget file type and the API version information required to run the gadget.

                Attributes:

                -   Type. Required. The expected value is "HTML".
                -   Src. Required. Specifies the file Sidebar should load to run the gadget.

            -   **&lt;permissions&gt; Element**

                Required.

                The expected value is "Full".

            -   **&lt;platform&gt; Element**

                Required.

                Specifies the minimum Sidebar version required to run the gadget.

                Attribute:

                -   MinPlatformVersion. Required. The expected value is "1.0".

            -   **&lt;autoscaleDPI&gt; element**

                For Windows 7, this optional node has been added that can contain a boolean value of either true or false (default). When set to true, the adaptive Zoom feature of the Windows Internet Explorer rendering engine is enabled, which causes all text and images for this gadget to be scaled to match the dots per inch (DPI) settings of the current user. When set to false (or the node is not included in the manifest), the Zoom feature is not enabled.

            -   **&lt;defaultImage&gt; Element**

                Optional.

                Specifies the graphic to display as the user drags the gadget from the gadget picker (before the gadget is instantiated) to the Sidebar.

                Attribute:

                -   src. Required. The path to the graphic file.

    -   **&lt;namespace&gt; Element**

        Optional.

        Reserved for future use.

    -   **&lt;author&gt; Element**

        Optional.

        Specifies developer-specific information.

        Attribute:

        -   name. Required. The gadget author's name.

        Elements:

        -   **&lt;info&gt; Element**

            Optional.

            Specifies extended developer-specific information.

            Attributes:

            -   url. Required. A hyperlink to a site specified by the author.
            -   text. Optional. The link text. If none specified, defaults to the value of the 'url' attribute.

        -   **&lt;logo&gt; Element**

            Optional.

            Specifies a graphic or icon associated with the developer that is displayed next to the author's name in the gadget picker details.

            Attribute:

            -   src. Required. The path to the graphic file.

    -   **&lt;copyright&gt; Element**

        Optional.

        Displayed to the user in various locations. It can contain any character string.

    -   **&lt;description&gt; Element**

        Optional.

        Displayed to the user in the Gadget Gallery dialog box.

    -   **&lt;icon&gt;**

        Optional.

        Specifies information for the gadget icon. The graphics file can be any file that's supported by GDI+ 1.0.

        A gadget manifest can contain any number of &lt;icon&gt; elements.

        Attributes:

        -   Src. Required. The path to the graphic file.
        -   Height. Optional. Integer specifying the height, in pixels, of the icon graphics file.
        -   Width. Optional. Integer specifying the width, in pixels, of the icon graphics file.

        > [!Note]  
        > The optimal size for the icon graphic is 64 pixels by 64 pixels, but any sized graphic can be specified. If multiple versions of an icon exist, Sidebar will use an icon closest in size to that required for a particular purpose.

         

 

 




