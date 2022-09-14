---
title: Web Service Compiler Tool
description: To support service model, wsutil.exe generates header to be used in both client and service side. It generates C proxy file for client side, and C stub file for service side, as needed.
ms.assetid: 1c73297d-0d3d-421c-9e19-44a6012a5c65
keywords:
- Web Service Compiler Tool Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Web Service Compiler Tool

To support service model, wsutil.exe generates header to be used in both client and service side. It generates C proxy file for client side, and C stub file for service side, as needed.


To support [serialization](serialization.md), the compiler generates headers for element descriptions for global element definitions, and all type definition information in proxy file to be consumed by the serialization engine.

Usage

**WsUtil.exe \[command-line-switches \[switch-options\]:\]&lt;filename&gt;**

command-line-switches

Specifies WsUtil.exe compiler options. Switches can appear in any order. Dash ('-') and slash ('/') are treated as the same.

List of command line options

-   @filename Specifies that the input file should be treated as a response file. This option can be used multiple times, in any places in the argument list.
-   /wsdl:&lt;filename&gt;:<optional\_url> Specifies that the input file should be treated as a wsdl file. Multiple wsdl inputs are allowed and all specified wsdl files are processed. The optional\_url specifies the location where the metadata was retrieved from. If no optional\_url is specified, Wsutil generates a unique url internally. See also [Policy Support](policy-support.md).
-   /xsd:&lt;filename&gt; Specifies that the input filename should be treated as a schema file. Multiple xsd inputs are allowed and all specified schema files are processed.
-   /wsp:&lt;filename&gt;:<optional\_url> Specifies that the input filename should be treated as policy metadata. Multiple wsp inputs are allowed and all specified policy files are processed. The optional\_url specifies the location where the metadata was retrieved from. If no optional\_url is specified, Wsutil generates a unique url internally. Policy files are ignored if /nopolicy flag is specified. See also [Policy Support](policy-support.md).
-   /nopolicy Disable policy processing.
-   /out:&lt;dirname&gt; Specifies directory name for output files
-   /noclient Do not generate the client side stub.
-   /noservice Do not generate the service side stub.
-   /prefix:&lt;string&gt; Prepend specified string to all generated identifiers.
-   /fullname Prepend normalized filename to generated identifiers. By default only name specified in "name" attribute will be used to generate identifiers for related descriptions.
-   /string:<WS\_STRING>\|<WCHAR\*> By default, wsutil generates WCHAR\* for xsd:string type. Application can use this flag to overwrite that behavior, and generates WS\_STRING for xsd:type instead.
-   /help Display help message
-   /? Same as /help
-   /W:x Error handling options. Could be W:0-W:4 \| WX
-   /nologo Do not generate compiler specific information on console output.
-   /nostamp Do not generate compiler specific information on generated files.

By default, the compiler generates the following files for WSDL file, or WSDL returned from metadata exchange:

-   Client proxy ({inputfilename}.c)
-   Service Stub ({inputfilename}.c)
-   Header file ({inputfilename}.h)

    The root of the generated filename is the input file name. Original input file extensions are preserved to prevent file name collision for generated files. By default client and service stubs are generated in the same file, with service stub code generated after the proxy code.

    By default, the compiler generates the following files for a XSD file for schema returned from metadata exchange:

-   serialization descriptions ({inputfilename}.c)
-   Header file ({inputfilename}.h)

    The root of the filename is the service name.

Wsutil.exe generates a "stamp" section at the beginning of all the generated files, indicating the compiler option, tool version, command line option applicable, etc. This section can be turned off by using /nostamp option to avoid noise with comparing generated files.

Wsutil does not support downloading metadata

Wsutil compiler works from local metadata file only. The tool does not support downloading metadata from running web services. Developers can use other supported webservice tools, like svcutil, to download metadata to local machine, inspect the saved files, and pass those files to wsutil.exe for compilation.

Multiple input/output file support

WSDL and XML schema allows including/importing definitions from other name spaces specified in other location/files. Wsutil supports multiple schema/wsdl/policy input, and generate one set of stub/header for each input files. Wsutil does not follow through the include and import statements. Instead, application should pass in files containing all necessary namespaces to wsutil such that the tool can resolve all dependencies during compilation.

**WsUtil.exe /xsd:stockquote.xsd /wsdl:stockquote.wsdl /wsdl:stockquoteservice.wsdl**

wsutil generates three sets of output files:

-   stockquote.xsd.c stockquote.xsd.h
-   stockquote.wsdl.c stockquote.wsdl.h
-   stockquoteservice.wsdl.h stockquoteservices.wsdl.c

Output file format

For each output file, wsutil generates externally available definitions in the header file. Other than C structure definitions and stub function prototypes, all the other web services related definitions are encapsulated in a global structure named with normalized filename.

``` syntax
typedef struct _stockquote_wsdl {
  struct {
  ... // list of WS_STRUCT_DESCRIPTION for all global complex types.
  } globalTypes;
  struct {
  ... // WS_ELEMENT_DESCRIPTION for all global elements.
  } globalElements;
  struct {
  ...
  } messages;
  struct {
  ...
  } contracts;
} _stockquote_wsdl;

EXTERN_C _stockquote_wsdl stockquote_wsdl;
```

Notice that not all the fields are generated for the global structure. A top level field is generated only when the related definitions are specified in the input file. For example, no message, operations, and contracts fields are generated for xsd files.

Warning Levels and error level

Similar to C compiler, WsUtil.exe supports four warning levels and one error level:

-   WsUtil.exe generates errors with unrecoverable failures, like invalid wsdl file, invalid compiler options etc.
-   WsUtil generates W1 warnings with serious recoverable issues. The compiler can go on but user should be aware of the issue. For example, a W1 warning will be generated if there are unsupported attributes, like some WSDL facets, in wsdl that does not affect code generation.
-   WsUtil generates W2 warnings with less serious problems. There is no lost of functionality, but application developer might want to know that. Like behaviors that might be different from other platforms.
-   WsUtil generates W3 warnings with minimal impact on generated code. For example, wsutil.exe generates a W3 warning when normalized string is different from original string.
-   W4 warning is more like "informational" warnings, and WsUtil issue W4 in cases like ignoring documentation attribute in WSDL.
-   WX indicates the compiler treats warning as error. For example, wsutil generates error for all W1 warnings if /W:1 /WX is specified.

/W:{N} specify which level of warning message should be generated. /W:1 means warning level 1 warnings should be generated, and warnings of warning level 2 and below should be masked and not generated by the tool.

## /fullname

This option indicates that WsUtil.exe generates full name for identifiers to avoid potential name collision. For example, in example.xsd we have:

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:types>
  <xs:element name="SimpleStruct">
   <xs:complexType>
    <xs:sequence>
     <xs:element name="a" type="xs:int" />
     <xs:element name="b" type="xs:int" />
    </xs:sequence>
   </xs:complexType>
  </xs:element>
 </wsdl:types>
</wsdl:definitions>
```

By default WsUtil.exe generates:

``` syntax
typedef struct SimpleStruct {
  int a;
  int b;
};
```

But if /fullname command line option is specified, WsUtil.exe generates the following structure definition instead:

``` syntax
typedef struct exmaple_xsd_SimpleStruct {
  int a;
  int b;
};
```

## Globalization

The tool is language neutral and can be localized to different languages. All error messages / console output can be localized. However, the command line options remain in English.

## Environment Variable

WsUtil.exe does not use any environment variables.

## Platform independent

Output files from WsUtil.exe are platform independent. There is no architecture dependent code generated in the stub; anything architecture specific will be taken care of by the C compiler. The stub can be used in all the platforms we support.

Description for wsutil.exe output can be found at [WSDL support](wsdl-support.md) and [Schema support](schema-support.md) part.

 

 




