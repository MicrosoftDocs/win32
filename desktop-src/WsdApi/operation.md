---
Description: 'Specifies an operation for which code is to be generated.'
ms.assetid: '559c7fcd-9652-4dfa-b22a-45929b6aee14'
title: operation element
---

# operation element

Specifies an operation for which code is to be generated.

## Usage

``` syntax
<operation/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                                                                 | Description                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**functionDeclarations**](functiondeclarations.md)<br/>                                         | Generates implementation declarations for proxy functions for port type operations.<br/> <br/>                                    |
| [**idlFunctionDeclarations**](idlfunctiondeclarations.md)<br/>                                   | Generates IDL declarations for proxy functions for port type operations.<br/> <br/>                                               |
| [**messageStructureDefinitions**](messagestructuredefinitions.md)<br/>                           | Generates C structure definitions for message types.<br/> <br/>                                                                   |
| [**messageTypeDeclarations**](messagetypedeclarations.md)<br/>                                   | Generates C constant declarations for XML schema tables for message types.<br/> <br/>                                             |
| [**messageTypeDefinitions**](messagetypedefinitions.md)<br/>                                     | Generates C constants for XML schema tables for message types.<br/> <br/>                                                         |
| [**portTypeDeclarations**](porttypedeclarations.md)<br/>                                         | Generates C constant declarations for port types.<br/> <br/>                                                                      |
| [**portTypeDefinitions**](porttypedefinitions.md)<br/>                                           | Generates C constants for port types.<br/> <br/>                                                                                  |
| [**proxyFunctionImplementations**](proxyfunctionimplementations.md)<br/>                         | Generates implementations for proxy functions for port type operations.<br/> <br/>                                                |
| [**stubDeclarations**](stubdeclarations.md)<br/>                                                 | Generates declarations for stub functions for port type operations.<br/> <br/>                                                    |
| [**stubDefinitions**](stubdefinitions.md)<br/>                                                   | Generates implementations for stub functions for port type operations.<br/> <br/>                                                 |
| [**subscriptionFunctionDeclarations**](subscriptionfunctiondeclarations.md)<br/>                 | Generates implementation declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/> |
| [**subscriptionIdlFunctionDeclarations**](subscriptionidlfunctiondeclarations.md)<br/>           | Generates IDL declarations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>            |
| [**subscriptionProxyFunctionImplementations**](subscriptionproxyfunctionimplementations.md)<br/> | Generates implementations for subscribe/unsubscribe proxy functions for port type notification operations.<br/> <br/>             |



## Remarks

Any number of operations may be specified. If no operations are specified, code is generated for all operations in all the relevant port types. Using the **operation** element will limit the methods generated to those contained in the operation.

For example, a printer supports these operations among others:

-   **PrintJobByPost**
-   **PrintJobByReference**
-   **CancelJob**
-   **GetJobElements**
-   **GetActiveJobs**
-   **GetJobHistory**
-   **SubscribeToPrinterConfigChange**
-   **UnsubscribeToPrinterConfigChange**

However, to include only the methods related to the **PrintJobByPost** and **GetJobElements** operations, the code generation script would use the [**idlFunctionDeclarations**](idlfunctiondeclarations.md) elements as follows:

``` syntax
<idlFunctionDeclarations>
    <operation>PrintJobByPost</operation>
    <operation>GetJobElements></operation>
</idlFunctionDeclarations>
```

This generates idl function declarations for all methods associated with the two operations (for example, **BeginPrintJobByPost**, **EndPrintJobByPost**, **BeginGetJobElements** and **EndGetJobElements**).

## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




