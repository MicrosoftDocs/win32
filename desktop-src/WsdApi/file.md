---
description: Directs the code generator to generate a file and specifies the output file name.
ms.assetid: d2ee6886-995f-453d-8121-f849b2d910ec
title: file element
ms.topic: reference
ms.date: 05/31/2018
---

# file element

Directs the code generator to generate a file and specifies the output file name.

## Usage

``` syntax
<file
  name = "pathname string">
  child elements
</file>
```

## Attributes



| Attribute           | Type                       | Required       | Description                                                                                                                         |
|---------------------|----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **name**<br/> | pathname string<br/> | Yes<br/> | The output filename for the generated content. The filename string should include complete path information.<br/> <br/> |



## Child elements



| Element                                                                                                 | Description                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDATA**<br/>                                                                                    | Text and CDATA sections are copied to the file without modification. Source code that is not a function of the contract input data can be added to output files using text and CDATA sections.<br/> <br/> |
| [**enumerationValueDeclarations**](enumerationvaluedeclarations.md)<br/>                         | Generates C declarations for values of all enumerated types.<br/> <br/>                                                                                                                                   |
| [**eventSourceBuilderDeclarations**](eventsourcebuilderdeclarations.md)<br/>                     | Generates declarations for functions that create event source classes.<br/> <br/>                                                                                                                         |
| [**eventSourceBuilderImplementations**](eventsourcebuilderimplementations.md)<br/>               | Generates functions that create event source classes.<br/> <br/>                                                                                                                                          |
| [**functionDeclarations**](functiondeclarations.md)<br/>                                         | Generates implementation declarations for proxy functions for port type operations.<br/> <br/>                                                                                                            |
| [**hostBuilderDeclaration**](hostbuilderdeclaration.md)<br/>                                     | Generates a declaration for a function that creates a typed host.<br/> <br/>                                                                                                                              |
| [**hostBuilderImplementation**](hostbuilderimplementation.md)<br/>                               | Generates a function that creates a typed host.<br/> <br/>                                                                                                                                                |
| [**idlFunctionDeclarations**](idlfunctiondeclarations.md)<br/>                                   | Generates IDL declarations for proxy functions for port type operations.<br/> <br/>                                                                                                                       |
| [**include**](include.md)<br/>                                                                   | Includes the contents of a macro or file in the generated output.<br/> <br/>                                                                                                                              |
| [**IUnknownDeclarations**](iunknowndeclarations.md)<br/>                                         | Generates declarations for QueryInterface, AddRef and Release.<br/> <br/>                                                                                                                                 |
| [**IUnknownDefinitions**](iunknowndefinitions.md)<br/>                                           | Generates implementations for QueryInterface, AddRef and Release.<br/> <br/>                                                                                                                              |
| [**literalInclude**](literalinclude.md)<br/>                                                     | Places a C or IDL include statement in the generated code. <br/> <br/>                                                                                                                                    |
| [**messageStructureDefinitions**](messagestructuredefinitions.md)<br/>                           | Generates C structure definitions for message types.<br/> <br/>                                                                                                                                           |
| [**messageTypeDeclarations**](messagetypedeclarations.md)<br/>                                   | Generates C constant declarations for XML schema tables for message types.<br/> <br/>                                                                                                                     |
| [**messageTypeDefinitions**](messagetypedefinitions.md)<br/>                                     | Generates C constants for XML schema tables for message types.<br/> <br/>                                                                                                                                 |
| [**namespaceDeclarations**](namespacedeclarations.md)<br/>                                       | Generates C declarations for namespace tables.<br/> <br/>                                                                                                                                                 |
| [**namespaceDefinitions**](namespacedefinitions.md)<br/>                                         | Generates C definitions for namespace tables.<br/> <br/>                                                                                                                                                  |
| [**portTypeDeclarations**](porttypedeclarations.md)<br/>                                         | Generates C constant declarations for port types.<br/> <br/>                                                                                                                                              |
| [**portTypeDefinitions**](porttypedefinitions.md)<br/>                                           | Generates C constants for port types.<br/> <br/>                                                                                                                                                          |
| [**proxyBuilderDeclarations**](proxybuilderdeclarations.md)<br/>                                 | Generates declarations for functions to create typed proxies.<br/> <br/>                                                                                                                                  |
| [**proxyBuilderImplementations**](proxybuilderimplementations.md)<br/>                           | Generates functions to create typed proxies.<br/> <br/>                                                                                                                                                   |
| [**proxyFunctionImplementations**](proxyfunctionimplementations.md)<br/>                         | Generates implementations for proxy functions for port type operations.<br/> <br/>                                                                                                                        |
| [**relationshipMetadataDeclaration**](relationshipmetadatadeclaration.md)<br/>                   | Generates a forward declaration for the hosting metadata specified in the [**hostMetadata**](hostmetadata.md) element. <br/> <br/>                                                                       |
| [**relationshipMetadataDefinition**](relationshipmetadatadefinition.md)<br/>                     | Generates a C constant definition for the hosting metadata specified in the [**hostMetadata**](hostmetadata.md) element. <br/> <br/>                                                                     |
| [**structDeclarations**](structdeclarations.md)<br/>                                             | Generates C structure declarations for known types.<br/> <br/>                                                                                                                                            |
| [**structDefinitions**](structdefinitions.md)<br/>                                               | Generates C structure definitions for known types.<br/> <br/>                                                                                                                                             |
| [**stubDeclarations**](stubdeclarations.md)<br/>                                                 | Generates declarations for stub functions for port type operations.<br/> <br/>                                                                                                                            |
| [**stubDefinitions**](stubdefinitions.md)<br/>                                                   | Generates implementations for stub functions for port type operations.<br/> <br/>                                                                                                                         |
| [**subscriptionFunctionDeclarations**](subscriptionfunctiondeclarations.md)<br/>                 | Generates implementation declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>                                                                         |
| [**subscriptionIdlFunctionDeclarations**](subscriptionidlfunctiondeclarations.md)<br/>           | Generates IDL declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>                                                                                    |
| [**subscriptionProxyFunctionImplementations**](subscriptionproxyfunctionimplementations.md)<br/> | Generates implementations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>                                                                                     |
| **text**<br/>                                                                                     | Text and CDATA sections are copied to the file without modification. Source code that is not a function of the contract input data can be added to output files using text and CDATA sections.<br/> <br/> |
| [**thisModelMetadataDeclaration**](thismodelmetadatadeclaration.md)<br/>                         | Generates a forward declaration for the C constant for the manufacturer metadata specified in the [**thisModelMetadata**](thismodelmetadata.md) element.<br/> <br/>                                      |
| [**thisModelMetadataDefinition**](thismodelmetadatadefinition.md)<br/>                           | Generates a C constant for the manufacturer metadata specified in the [**thisModelMetadata**](thismodelmetadata.md) element.<br/> <br/>                                                                  |
| [**typeTableDeclarations**](typetabledeclarations.md)<br/>                                       | Generates C constant declarations for XML schema tables for known types.<br/> <br/>                                                                                                                       |
| [**typeTableDefinitions**](typetabledefinitions.md)<br/>                                         | Generates C constants for XML schema tables for known types.<br/> <br/>                                                                                                                                   |



### Child element sequence

``` syntax
(
  text, 
  CDATA, 
  namespaceDeclarations*, 
  namespaceDefinitions*, 
  structDeclarations*, 
  structDefinitions*, 
  typeTableDeclarations*, 
  typeTableDefinitions*, 
  thisModelMetadataDeclaration*, 
  thisModelMetadataDefinition*, 
  portTypeDeclarations*, 
  portTypeDefinitions*, 
  messageStructureDefinitions*, 
  messageTypeDeclarations*, 
  messageTypeDefinitions*, 
  idlFunctionDeclarations*, 
  subscriptionIdlFunctionDeclarations*, 
  functionDeclarations*, 
  subscriptionFunctionDeclarations*, 
  proxyFunctionImplementations*, 
  subscriptionProxyFunctionImplementations*, 
  stubDeclarations*, 
  stubDefinitions*, 
  enumerationValueDeclarations*, 
  include*, 
  IUnknownDeclarations*, 
  IUnknownDefinitions*, 
  relationshipMetadataDeclaration*, 
  relationshipMetadataDefinition*, 
  proxyBuilderDeclarations*, 
  proxyBuilderImplementations*, 
  hostBuilderDeclaration*, 
  hostBuilderImplementation*, 
  eventSourceBuilderDeclarations*, 
  eventSourceBuilderImplementations*, 
  literalInclude*
)
```

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

The name of the file is determined by the value of the name attribute or child element. The content of the file is determined by the other child elements, text and CDATA in the **file** element. Text and CDATA are copied to the file unmodified. Child elements are replaced with generated code. Text, CDATA and child elements may occur in any order and may be repeated indefinitely.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | No            |



 

 




