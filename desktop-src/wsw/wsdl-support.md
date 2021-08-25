---
title: WSDL and Service Contracts
description: The Wsutil.exe utility generates a C language stub according to supplied WSDL metadata, as well as data type definitions and descriptions for data types described by user-authored XML schemas.
ms.assetid: d3c147d6-e370-4e8a-96d8-6660f3a2b996
keywords:
- WSDL support
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# WSDL and Service Contracts

The [Wsutil.exe](web-service-compiler-tool.md) utility generates a C language stub according to supplied WSDL metadata, as well as data type definitions and descriptions for data types described by user-authored XML schemas.


The following is an example WSDL document and XML schema that serves as a basis for the discussion that follows:

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:types>
  <xs:schema xmlns:tns="http://Example.org" elementFormDefault="qualified" 
  targetNamespace="http://Example.org" xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <xs:element name="SimpleMethod">
    <xs:complexType>
     <xs:sequence>
      <xs:element name="a" type="xs:int" />
      <xs:element name="b" type="xs:int" />
     </xs:sequence>
    </xs:complexType>
   </xs:element>
   <xs:element name="SimpleMethodResponse">
    <xs:complexType>
     <xs:sequence>
      <xs:element name="b" type="xs:int" />
      <xs:element name="c" type="xs:int" />
     </xs:sequence>
    </xs:complexType>
   </xs:element>
  </xs:schema>
 </wsdl:types>
 <wsdl:message name="ISimpleService_SimpleMethod_InputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethod" />
 </wsdl:message>
 <wsdl:message name="ISimpleService_SimpleMethod_OutputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethodResponse" />
 </wsdl:message>
 <wsdl:portType name="ISimpleService">
  <wsdl:operation name="SimpleMethod">
   <wsdl:input wsaw:Action="http://Example.org/ISimpleService/SimpleMethod" 
   message="tns:ISimpleService_SimpleMethod_InputMessage" />
   <wsdl:output wsaw:Action="http://Example.org/ISimpleService/SimpleMethodResponse" 
   message="tns:ISimpleService_SimpleMethod_OutputMessage" />
  </wsdl:operation>
 </wsdl:portType>
 <wsdl:binding name="DefaultBinding_ISimpleService" type="tns:ISimpleService">
  <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
  <wsdl:operation name="SimpleMethod">
   <soap:operation soapAction="http://Example.org/ISimpleService/SimpleMethod" 
   style="document" />
   <wsdl:input>
    <soap:body use="literal" />
   </wsdl:input>
   <wsdl:output>
    <soap:body use="literal" />
   </wsdl:output>
  </wsdl:operation>
 </wsdl:binding>
 <wsdl:service name="SimpleService">
  <wsdl:port name="ISimpleService" binding="tns:DefaultBinding_ISimpleService">
   <soap:address location="http://Example.org/ISimpleService" />
  </wsdl:port>
 </wsdl:service>
</wsdl:definitions>
```

This example provides a contract, ISimpleService, with a single method, SimpleMethod. "SimpleMethod" has two input parameters of type **integer**, *a* and *b*, that are sent from the client to the service. Likewise, SimpleMethod has two output parameters of type **integer**, *b* and *c*, which are returned to the client after successful completion. In SAL-annotated C syntax, the method definition appears as follows:

``` syntax
void SimpleMethod(__in int a, __inout int *  b, __out int * c );
```

In this definition, ISimpleService is a service contract with a single service operation: SimpleMethod.

The output header file contains definitions and descriptions for external reference. This includes:

-   C structure definitions for global element types.
-   An operation prototype as defined in current file.
-   A function table prototype for the contracts specified in the WSDL file.
-   Client proxy and service stub prototypes for all the functions specified in current file.
-   A [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description) data structure for the global schema elements defined in current file.
-   A [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description) data structure for all the messages specified in current file.
-   A [**WS\_CONTRACT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_contract_description) data structure for all the contracts specified in current file.

One global structure is generated to encapsulate all the global descriptions for the schema types and service model types to which the application can refer. The structure is named using a normalized file name. In this example, Wsutil.exe generates a global definitions structure named "example\_wsdl" that contains all the web service descriptions. The structure definition is generated in the stub file.

``` syntax
typedef struct _example_wsdl
{
  struct {
    WS_ELEMENT_DESCRIPTION SimpleMethod;
    WS_ELEMENT_DESCRIPTION SimpleMethodResponse;
  } elements;
  struct {
    WS_MESSAGE_DESCRIPTION ISimpleService_SimpleMethod_InputMessage;
    WS_MESSAGE_DESCRIPTION ISimpleService_SimpleMethod_OutputMessage;
  } messages;
  struct {
    WS_CONTRACT_DESCRIPTION DefaultBinding_ISimpleService;
  } contracts;
} _example_wsdl;

extern const _stockquote_wsdl stockquote_wsdl;
```

For global element definitions in the XML schema document (XSD), one [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description) prototype, as well as the corresponding C type definition, are generated for each of the elements. The prototypes for the element descriptions for SimpleMethod and SimpleMethodResponse are generated as members in the structure above. The C structures are generated as follows:

``` syntax
typedef struct SimpleMethod
{
  int   a;
  int   b;
} SimpleMethod;

typedef struct SimpleMethodResponse
{
  int   b;
  int   c;
} SimpleMethodResponse;
```

Similarly for global complex types, Wsutil.exe generates type C structure definitions like above, without matching element descriptions.

For WSDL input, Wsutil.exe generates the following prototypes and definitions:

-   A [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description) prototype is generated for the message description. This description can be used by the service model as well as the message layer. Message description structures are fields named "messagename" in the global structure. In this example, the message description is generated as the ISimpleService\_SimpleMethod\_InputMessage field in the ISimpleService\_SimpleMethod\_InputMessage structure as specified in the WSDL file.
-   [**WS\_CONTRACT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_contract_description) prototype is generated for the contract description. This description is used by service model. Contract description structures are fields named "contractname" in the global structure. In this example, the contract description is generated as the DefaultBinding\_ISimpleService field in the structure "\_example\_wsdl".

Operation and type specifications are common to both proxy and stub and they are generated in both files. Wsutil.exe generates one copy only if both the proxy and stub are generated in the same file.

## Identifier generation

The autogenerated C structures listed above are created based on the name specified in WSDL file. An XML NCName is not commonly considered a valid C identifier, and the names are normalized as needed. Hex values are not converted, and common letters like ':', '/' and '.' are converted to the underscore '\_' character to improve readability.

## Header for the stub

For each operation in the service contract, one callback routine named "&lt;operationname&gt;Callback" is generated. (For example, the operation "SimpleMethod" in the example service contract has a generated callback named "SimpleMethodCallback".)

``` syntax
typedef HRESULT (CALLBACK *SimpleMethodCallback) (
  const WS_OPERATION_CONTEXT * context,
  int a, int *b, int *c,
  const WS_ASYNC_CONTEXT *asyncContext,
  WS_ERROR * error);
```

For each WSDL **portType** Wsutil.exe generates a function table representing **portType**. Each operation on the **portType** has a corresponding function pointer to the callback present in the function table.

``` syntax
struct ISimpleServiceMethodTable
{
  ISimpleService_SimpleMethodCallback SimpleMethod;
};
```

Proxy prototypes are generated for all operations. The prototype name is the operation name (in this case, "SimpleMethod") specified in WSDL file for the service contract.

``` syntax
HRESULT WINAPI SimpleMethod(WS_CHANNEL *channel,
  WS_HEAP *heap,
  int a,
  int *b,
  int *c,
  const WS_ASYNC_CONTEXT * asyncContext,
  WS_ERROR * error );
```

## Local-only Description Prototype Generation

The proxy andstub files contain the definition for the global definitions structure, including prototypes and definitions for the structures containing local-only descriptions and client proxy/service stub implementations.

All prototypes and definitions that are local to the stub file are generated as part of an encapsulating structure. This overarching local description structure provides a clear hierarchy of the descriptions required by the serialization layer and the service model. The local description structure has prototypes similar to the one shown below:

``` syntax
struct _filenameLocalDefinitions
{
  struct {
  // schema related output for all the embedded 
  // descriptions that needs to describe global complex types.
  } globalTypes;
  // global elements.
  struct {
  // schema related output, like field description
  // structure description, element description etc.
  ...
  } globalElements;
  struct {
  // messages and related descriptions
  } messages;
  struct {
  // contract and related descriptions.
  } contracts;
  struct {
  // XML dictionary entries.
  } dictionary;
} _filenameLocalDefinitions;
```

## Referencing definitions from other files

Local definitions can reference descriptions generated in another file. For example, the message may be defined in the C code file generated from the WSDL file but the message element may be defined elsewhere in the C code file generated from the XSD file. In this case, Wsutil.exe generates reference to the global element from the file that contains the message definition, as demonstrated below:

``` syntax
{  // WS_MESSAGE_DESCRIPTION
...
(WS_ELEMENT_DESRIPTION *)b_xsd.globalElement.<elementname>
  };
```

## Global element descriptions

For each global element defined in a wsdl:type or XSD file, there is a matching field named **elementName** inside the **GlobalElement** field. In this example, a structure named SimpleMethod is generated:

``` syntax
typedef struct _SimpleServiceLocal
{
  struct  // global elements
  {
    struct // SimpleMethod
    {
    ...
    WS_ELEMENT_DESCRIPTION SimpleMethod;
    } SimpleMethod;
    ...
  } globalElements;
}
```

Other descriptions required by the element description are generated as part of the containing structure. If the element is a simple type element, there is only one [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description) field. If the element type is a structure, all of the related fields and structure descriptions are generated as part of the element structure. In this example, SimpleMethod element is a structure containing two fields, **a** and **b**. Wsutil.exe generates the structure as follows:

``` syntax
...
struct // SimpleMethod
{
  struct // SimpleMethod structure
  {
    WS_FIELD_DESCRIPTION a;
    WS_FIELD_DESCRIPTION b;
    WS_FIELD_DESCRIPTION * SimpleMethodFields [2];
    WS_STRUCT_DESCRIPTION structDesc;
  } SimpleMethoddescs; // SimpleMethod
  WS_ELEMENT_DESCRIPTION elementDesc;
} SimpleMethod;
...
```

Embedded structures and embedded elements are generated as sub-structures as needed.

## WSDL related definitions

Wsutil.exe generates a field under WSDL section for each of the **portType** values defined under the specified wsdl:service.

``` syntax
...
struct { // WSDL
    struct { // portTypeName
        struct { // operationName
        } operationName;
    ...
    WS_OPERATION_DESCRIPTION* operations[numOperations];
    WS_CONTRACT_DESCRIPTION contractDesc;
    } portTypeName;
}
...
```

Wsutil.exe generates one field f that contains all the descriptions needed for the operation, a signle array of pointers to each of the operation descriptions for each method, and one [**WS\_CONTRACT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_contract_description) for the specified **portType**.

All the descriptions needed by operations are generated inside the **operationName** field under the specified **portType**. These include the [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description) field as well as the sub-structure for input and output parameter s. Likewise, the [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description) fields for the input message and the optional output message are included along with the; [**WS\_PARAMETER\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_parameter_description) list field for all of the operation parameters and the [**WS\_OPERATION\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_operation_description) field for the operation itself. In this example, the code structure for the SimpleMethod description is generated as seen below:

``` syntax
...
struct // messages
{
  WS_MESSAGE_DESCRIPTION ISimpleService_SimpleMethod_InputMessage;
  WS_MESSAGE_DESCRIPTION ISimpleService_SimpleMethod_OutputMessage;
} messages;
struct // contracts
{
  struct // DefaultBinding_ISimpleService
  {
    struct // SimpleMethod
    {
      WS_PARAMETER_DESCRIPTION params[3];
      WS_OPERATION_DESCRIPTION SimpleMethod;
    } SimpleMethod;
    WS_OPERATION_DESCRIPTION* operations[1];
    WS_CONTRACT_DESCRIPTION contractDesc;
  } DefaultBinding_ISimpleService;
} contracts;
...
```

## XML dictionary related definitions

Names and namespaces used in various descriptions are generated as fields of type [**WS\_XML\_STRING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_string). All of these strings are generated as part a per-file constant dictionary. The list of strings and the [**WS\_XML\_DICTIONARY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_dictionary) field (named **dict** in the example below) are generated as part of the dictionary field of the **fileNameLocal** structure.

``` syntax
struct { // fileNameLocal
...
  struct { // dictionary
    struct { // XML string list
      WS_XML_STRING firstFieldName;
      WS_XML_STRING firstFieldNS;
      ...
    } xmlStrings;
  WS_XML_DICTIONARY dict;
  } dictionary;
}; // fileNameLocal;
```

The array of [**WS\_XML\_STRING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_string)s are generated as a series of fields of type **WS\_XML\_STRING**, named with with user-friendly names. The generated stub uses the user-friendly names in various descriptions for better readability.

Client proxy for WSDL operations

Wsutil.exe generates a client proxy for all of the operations. Applications can overwrite the method signature using a prefix command-line option.

``` syntax
HRESULT WINAPI bindingName_SimpleMethod(WS_SERVICE_PROXY *serviceProxy,
  WS_HEAP *heap,
  int a,
  int *b,
  int *c,
  const WS_CALL_PROPERTY* callProperties,
  ULONG callPropertyCount,
  const WS_ASYNC_CONTEXT * asyncContext,
  WS_ERROR * error )
{
  void* argList[] = {&a, &b, &c};
  return WsCall(_serviceProxy,
    (WS_OPERATION_DESCRIPTION*)&example_wsdlLocalDefinitions.contracts.DefaultBinding_ISimpleService.SimpleMethod.SimpleMethod,
    (void **)&_argList,
    callProperties,
    callPropertyCount,
    heap,
    asyncContext,
    error
  );      
}
```

The operation caller must pass in a valid *heap* parameter. Output parameters are allocated using the WS\_HEAP value specified in the *heap* parameter. The calling function can reset or free the heap to release memory for all of the output parameters. If the operation fails, additional detail error information can be retrieved from the optional error object if it is available.

Wsutil.exe generates a service stub for all of the operations described in binding.

``` syntax
HRESULT CALLBACK ISimpleService_SimpleMethodStub(
  const WS_OPERATION_CONTEXT *context,
  void * stackStruct,
  void * callback,
  const WS_ASYNC_CONTEXT * asyncContext,
  WS_ERROR *error )
{
  SimpleMethodParamStruct *pstack = (SimpleMethodParamStruct *) stackstruct;
  SimpleMethodOperation operation = (SimpleMethodOperation)callback;
  return operation(context, pstack->a, &(pstack->b), &(pstack->c ), asyncContext, error );
}
```

The above section describes the prototype of the local structure containing all of the definitions local to the stub file only. Subsequent sections describe the definitions of the descriptions.

## WSDL Definition Generation

Wsutil.exe generates a constant static (**const static**) structure named *<file\_name>*LocalDefinitions of type *<service\_name>*Local that contains all the local only definitions.

``` syntax
const static _SimpleServiceLocal example_wsdlLocalDefinitions =
{
  {  // global types
  ...
  }, // global types
  {  // global elements
  ...
  }, // global elements
  {  // messages
  ...
  }, //messages
  ...
  {  // dictionary
  ...
  }, // dictionary
},
```

The following WSDL descriptions are supported:

-   wsdl:service
-   wsdl:binding
-   wsdl:portType
-   wsdl:operation
-   wsdl:message

## Processing wsdl:operation and wsdl:message

Each operation specified in the WSDL document is mapped to a service operation by [Wsutil.exe](web-service-compiler-tool.md). The tool generates separate definitions of the service operations for both the server and the client.

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:portType name="ISimpleService">
  <wsdl:operation name="SimpleMethod">
   <wsdl:input wsaw:Action="http://Example.org/ISimpleService/SimpleMethod" 
   message="tns:ISimpleService_SimpleMethod_InputMessage" />
   <wsdl:output wsaw:Action="http://Example.org/ISimpleService/SimpleMethodResponse" 
   message="tns:ISimpleService_SimpleMethod_OutputMessage" />
  </wsdl:operation>
 </wsdl:portType>
 <wsdl:message name="ISimpleService_SimpleMethod_InputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethod" />
 </wsdl:message>
 <wsdl:message name="ISimpleService_SimpleMethod_OutputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethodResponse" />
 </wsdl:message>
</wsdl:definitions>
```

The layout of the input andoutput message data elements is evaluated by the tool to generate the serialization metadata for the infrastructure along with the actual signature of the resulting service operation to which the input and output messages are associated.

The metadata for each operation within a specific **portType** has input and optionally an output message, each of these messages is mapped to a [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description). In this example, the input and the output message on the operation in the portType mapped to inputMessageDescription and optionally the outputMessageDescription on the [**WS\_OPERATION\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_operation_description) respectively.

For each WSDL message the tool generates [**WS\_MESSAGE\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_message_description) that references the [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description) definition, as demonstrated below:

``` syntax
... 
{    // message description for ISimpleService_SimpleMethod_InputMessage
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.DefaultBinding_ISimpleServiceISimpleService_SimpleMethod_InputMessageactionName,
  (WS_ELEMENT_DESCRIPTION*)&(WS_ELEMENT_DESCRIPTION*)&example_wsdl.globalElements.SimpleMethodReponse
},  // message description for ISimpleService_SimpleMethod_InputMessage
...
```

The message description refers to the input element description. Because the element is globally defined, the message description references the global definition instead of the local static element. Similarly, if the element is defined in another file, Wsutil.exe generates a reference to the globally-defined structure in that file. For example, if SimpleMethodResponse is defined in another example.xsd file, Wsutil.exe generates the following instead:

``` syntax
...
{    // message description for ISimpleService_SimpleMethod_InputMessage
(WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.DefaultBinding_ISimpleServiceISimpleService_SimpleMethod_InputMessageactionName,
(WS_ELEMENT_DESCRIPTION*)&(WS_ELEMENT_DESCRIPTION*)&example_xsd.globalElements.SimpleMethodReponse
},  // message description for ISimpleService_SimpleMethod_InputMessage
...
```

Each message description contains the action and the specific element description (a field of type [**WS\_ELEMENT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_element_description)) for all the message data elements. In the case of an RPC-style message or a message with multiple parts, a wrapper element is created to encapsulate the additional information.

## RPC style support

Wsutil.exe supports document-style as well as RPC-style operations according to the WSDL 1.1 Binding Extension for SOAP 1.2 specification. RPC- and literal-style operations are marked as WS\_RPC\_LITERAL\_OPERATION. The service model ignores the name for the response body wrapper element in RPC/literal operations.

Wsutil.exe does not natively support encoding-style operations. The WS\_XML\_BUFFER parameter is generated for encoding messages, and developers must populate the opaque buffer directly.

## Multiple message parts support

Wsutil.exe supports multiple message parts in one message. A multi-part message can be specified as follows:

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:message name="ISimpleService_MutipleParts_InputMessage">
  <wsdl:part name="part1" element="tns:SimpleElement1" />
  <wsdl:part name="part2" element="tns:SimpleElement2" />
 </wsdl:message>
</wsdl:definitions>
```

Wsutil.exe generates a [**WS\_STRUCT\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_type) field for the message element if the message contains multiple parts. If the message is represented using the document style, Wsutil.exe generates a wrapper element with struct type. The wrapper element does not have a name or a specific namespace, and the wrapper structure contains all of the elements in all of the parts as fields. The wrapper element is for internal use only and it will not be serialized in the message body.

If the message is using RPC or literal style representation , Wsutil.exe creates a wrapper element with the operation name as the element name and the specified namespace as service namespace according to WSDL SOAP extension specification. The structure of the element contains an array of fields representing the types specified in the message parts. The wrapper element is mapped to the actual top element in message body as indicated in the SOAP specification.

On the server side, each operation results in a typedef of the resulting server service operation. This typedef is used to refer to the operation in the function table as described previously. Every operation also results in the generation of a stub function which nfrastructure calls on behalf of the delegate to the actual method.

``` syntax
typedef HRESULT (CALLBACK *SimpleMethodCallback) (
  const WS_OPERATION_CONTEXT* context,
  unsigned int  a,
  unsigned int * b,
  unsigned int * c,
  const WS_ASYNC_CONTEXT* asyncContext,
  WS_ERROR* error
  );
```

For the SimpleMethod operation, the SimpleMethodOperation typedef is defined above. Note that the generated method has an expanded argument listwith the message part for the input and output message for SimpleMethod operation as named parameters.

On the client side each operation is mapped to a proxy service operation.

``` syntax
HRESULT WINAPI SimpleMethod (
  WS_SERVICE_PROXY* serviceProxy,
  ws_heap *heap,
  unsigned int  a,
  unsigned int * b,
  unsigned int * c,
  const WS_ASYNC_CONTEXT* asyncContext,
  WS_ERROR* error);
```

## Processing wsdl:binding

The WWSAPI service model supports theSOAP binding extension. For each binding there is an associated **portType**.

The transport specified in soap binding extension is advisory only. Application needs to provide transport information when creating a channel. Currently we support the WS\_HTTP\_BINDING and WS\_TCP\_BINDING bindings.

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:binding name="DefaultBinding_ISimpleService" type="tns:ISimpleService">
  <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
  <wsdl:operation name="SimpleMethod">
   <soap:operation soapAction="http://Example.org/ISimpleService/SimpleMethod" 
   style="document" />
   <wsdl:input>
    <soap:body use="literal" />
   </wsdl:input>
   <wsdl:output>
    <soap:body use="literal" />
   </wsdl:output>
  </wsdl:operation>
 </wsdl:binding>
</wsdl:definitions>
```

In our example WSDL document we only have one **portType** for ISimpleService. The provided SOAP binding indicates the HTTP transport, which is specified as WS\_HTTP\_BINDING. Notice that this structure does not have static decoration as this structure needs to be available to the application.

Processing wsdl:portType

Each **portType** in WSDL is made up of one or more operations. The operation should be consistent with the SOAP binding extension indicated in wsdl:binding.

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:portType name="ISimpleService">
  <wsdl:operation name="SimpleMethod">
   ...
  </wsdl:operation>
 </wsdl:portType>
</wsdl:definitions>
```

In this example, the ISimpleService **portType** only contains the SimpleMethod operation. This is consistent with the binding section where there is only one WSDL operation that maps to a SOAP action.

Since the ISimpleService **portType** only has one operation -- SimpleMethod -- the corresponding function table only contains SimpleMethod as a service operation.

In terms of metadata each **portType** is mapped by Wsutil.exe to a [**WS\_CONTRACT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_contract_description). Each operation within a **portType** is mapped to a [**WS\_OPERATION\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_operation_description).

In this example, **portType** the tool generates [**WS\_CONTRACT\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_contract_description) for ISimpleService. This contract description contains the specific number of operations available on the ISimpleService **portType** along with an array of [**WS\_OPERATION\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_operation_description) representing the individual operations defined on the portType for ISimpleService. Since there is only one operation on ISimpleService portType for ISimpleService, there is also only one **WS\_OPERATION\_DESCRIPTION** definition.

``` syntax
...  part of LocalDefinitions structure
{    // array of operations for DefaultBinding_ISimpleService
(WS_OPERATION_DESCRIPTION*)&example_wsdlLocalDefinitions.contracts.DefaultBinding_ISimpleService.SimpleMethod.SimpleMethod,
},    // array of operations for DefaultBinding_ISimpleService
{    // contract description for DefaultBinding_ISimpleService
1,
(WS_OPERATION_DESCRIPTION**)example_wsdlLocalDefinitions.contracts.DefaultBinding_ISimpleService.operations,
WS_HTTP_CHANNEL_BINDING,
},  // end of contract description for DefaultBinding_ISimpleService
},    // DefaultBinding_ISimpleService       ...
```

## Processing wsdl:service

WsUtil.exe uses the services to find binding/porttypes, and generates contract structure that describes types, message, porttype definitions, and so on. Contract descriptions are externally accessible, and they are generated as part of the global definition structure specified through generated header.

WsUtil.exe supports EndpointReference extensions defined in wsdl:port. Endpoint reference is defined in WS-ADDRESSING as a way to describe [endpoint](endpoint-address.md) information of a service. The input endpoint reference extension text saved as [**WS\_XML\_STRING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_string), together with matching [**WS\_ENDPOINT\_ADDRESS\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_address_description) are generated in endpointReferences section in the global structure.

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:service name="SimpleService">
  <wsdl:port name="ISimpleService" binding="tns:DefaultBinding_ISimpleService">
   <soap:address location="http://Example.org/ISimpleService" />
   <wsa:EndpointReference>
    <wsa:Address>http://example.org/wcfmetadata/WSHttpNon</wsa:Address>
   </wsa:EndpointReference> 
  </wsdl:port>
 </wsdl:service>
</wsdl:definitions>
```

``` syntax
  const _example_wsdl example_wsdl =
  {
  ... // global element description
  {// messages
  {    // message description for ISimpleService_SimpleMethod_InputMessage
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.ISimpleService_SimpleMethod_InputMessageactionName,
  (WS_ELEMENT_DESCRIPTION*)&example_wsdl.globalElements.SimpleMethod,
},    // message description for ISimpleService_SimpleMethod_InputMessage
{    // message description for ISimpleService_SimpleMethod_OutputMessage
(WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.ISimpleService_SimpleMethod_OutputMessageactionName,
  (WS_ELEMENT_DESCRIPTION*)&example_wsdl.globalElements.SimpleMethodResponse,
},    // message description for ISimpleService_SimpleMethod_OutputMessage
}, // messages
{// contracts
{   // DefaultBinding_ISimpleService
1,
(WS_OPERATION_DESCRIPTION**)example_wsdlLocalDefinitions.contracts.DefaultBinding_ISimpleService.operations,
WS_HTTP_CHANNEL_BINDING,
},    // end of DefaultBinding_ISimpleService
    }, // contracts
    {
        {
            {   // endpointAddressDescription
                WS_ADDRESSING_VERSION_0_9,
            },                    
            (WS_XML_STRING*)&xml_string_generated_in_stub // endpointReferenceString
        }, //DefaultBinding_ISimpleService
    }, // endpointReferences
}
```

To Create [**WS\_ENDPOINT\_ADDRESS**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_address) using the WsUtil generated metadata:

``` syntax
WsCreateReader      // Create a WS_XML_READER
Initialize a WS_XML_READER_BUFFER_INPUT
WsSetInput          // Set the encoding and input of the reader to generated endpointReferenceString
WsReadType        // Read WS_ENDPOINT_ADDRESS from the reader
    // Using WS_ELEMENT_TYPE_MAPPING, WS_ENDPOINT_ADDRESS_TYPE and generated endpointAddressDescription, 
```

Constant strings in the client proxy or service stub are generated as fields of type WS\_XML\_STRING, and there is a constant dictionary for all the strings in the proxy or stub file. Each string in the dictionary is generated as a field in the dictionary part of the local structure for better readability.

``` syntax
... // dictionary part of LocalDefinitions structure
{    // xmlStrings
  { // xmlStrings
    WS_XML_STRING_DICTIONARY_VALUE("a",&example_wsdlLocalDefinitions.dictionary.dict, 0), 
    WS_XML_STRING_DICTIONARY_VALUE("http://Sapphire.org",&example_wsdlLocalDefinitions.dictionary.dict, 1), 
    WS_XML_STRING_DICTIONARY_VALUE("b",&example_wsdlLocalDefinitions.dictionary.dict, 2), 
    WS_XML_STRING_DICTIONARY_VALUE("SimpleMethod",&example_wsdlLocalDefinitions.dictionary.dict, 3),
    ...
  },  // end of xmlStrings
  {   // SimpleServicedictionary
    // 45026280-d5dc-4570-8195-4d66d13bfa34
    { 0x45026280, 0xd5dc, 0x4570, { 0x81, 0x95, 0x4d,0x66, 0xd1, 0x3b, 0xfa, 0x34 } },
    (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings,
    stringCount,
    TRUE,
  },
}
...
```

## Processing wsdl:type

Wsutil.exe only supports XML schema (XSD) documents in wsdl:type specification. One special case is when a message port specifies a global element definition. See the following section for more details of the heuristics used in these cases.

## Parameter Processing Heuristics

In the service model, WSDL messages are mapped to specific parameters in a method. Wsutil.exe has two styles of parameter generation: in first style, the operation has one parameter for input message, and one parameter for output message (if necessary); in the second style, Wsutil.exe uses a heuristic to map and expand fields in the structures for both input messages and output messages to different parameters in the operation. Both input and output messages need to have structure type message elements to generate this second approach.

Wsutil.exe uses the following rules when generating operation parameters from the input and output messages:

-   For input and output messages with multiple message parts, each message part is a separate parameter in the operation, with the message part name as parameter name.
-   For RPC style message with one message part, the message part is a parameter in the operation, with message part name as parameter name.
-   For document-style input and output messages with one message part:
    -   If the name of a message part is "parameters" and the element type is a structure, each field in the structure is treated as a separate parameter with the field name being the parameter name.
    -   If the message part name is not "parameters", the message is a parameter in the operation with the message name used as the corresponding parameter name.
-   For document style input and output message with nillable element, the message is mapped to one parameter, with message part name as parameter name. One additional level of indirection is added to indicate the pointer can be **NULL**.
-   If a field appears in the input message element only, the field is treated as an \[in\] parameter.
-   If a field appears in the output message element only, the field is treated as an \[out\] parameter.
-   If there is a field with the same name and same type that appears in both the input message and the output message, the field is treated as an \[in,out\] parameter.

Following tools are used to determine the direction of parameters:

-   If a field appears in input message element only, the field is treated as in only parameter.
-   If a field appears in output message element only, the field is treated as out only parameter.
-   If there is a field with the same name and same type that appears in both input message and output message, the field is treated as an in,out parameter.

Wsutil.exe only supports sequenced elements. It rejects invalid ordering with regard to \[in,out\] parameters if Wsutil.exe cannot combine the in parameters and out parameters into a single parameter list. Suffixes might be added to parameter names to avoid name collision.

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:message name="ISimpleService_SimpleMethod_InputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethod" />
 </wsdl:message>
 <wsdl:message name="ISimpleService_SimpleMethod_OutputMessage">
  <wsdl:part name="parameters" element="tns:SimpleMethodResponse" />
 </wsdl:message>
</wsdl:definitions>
```

Wsutil.exe considers fields in tns:SimpleMethod and tns:SimpleMethodResponse ato be parameters, as seen in the parameter definitions below:

``` syntax
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://Example.org" 
xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:xs="http://www.w3.org/2001/XMLSchema" 
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" targetNamespace="http://Example.org" 
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:types>
  <xs:schema xmlns:tns="http://Example.org" elementFormDefault="qualified" 
  targetNamespace="http://Example.org" xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <xs:import namespace="http://Example.org" />
   <xs:element name="SimpleMethod">
    <xs:complexType>
     <xs:sequence>
      <xs:element name="a" type="xs:unsignedInt" />
      <xs:element name="b" type="xs:unsignedInt" />
     </xs:sequence>
    </xs:complexType>
   </xs:element>
   <xs:element name="SimpleMethodResponse">
    <xs:complexType>
     <xs:sequence>
      <xs:element name="b" type="xs:unsignedInt" />
      <xs:element name="c" type="xs:unsignedInt" />
     </xs:sequence>
    </xs:complexType>
   </xs:element>
  </xs:schema>
 </wsdl:types>
</wsdl:definitions>
```

Wsutil.exe expands the parameter list from the fields in the list above, and generates the **ParamStruct** structure in the following code example. The service model run-time can use this structure to pass arguments to the client and server stubs.

``` syntax
typedef struct SimpleMethodParamStruct {
  unsigned int   a;  
  unsigned int   b;
  unsigned int   c;
} ;
```

This structure is only used to describe the stack frame on the client and server side. There is no change to the message description, or to the element descriptions referenced by the message description.

``` syntax
  // following are local definitions for the complex type
  { // field description for a
  WS_ELEMENT_FIELD_MAPPING,
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.aLocalName,
(WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.aNamespace,
  WS_INT32_TYPE,
  0,
  WsOffsetOf(_SimpleMethod, a),
  0,
  0,
  },    // end of field description for a
  { // field description for b
  WS_ELEMENT_FIELD_MAPPING,
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.bLocalName,
(WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.aNamespace,
  WS_INT32_TYPE,
  0,
  WsOffsetOf(_SimpleMethod, b),
  0,
  0,
  },    // end of field description for b
  {    // fields description for _SimpleMethod
  (WS_FIELD_DESCRIPTION *)&example_wsdlLocalDefinitions.globalElements.SimpleMethod._SimpleMethoddescs.a,
  (WS_FIELD_DESCRIPTION *)&example_wsdlLocalDefinitions.globalElements.SimpleMethod._SimpleMethoddescs.b,
  },
  {  // structure definition
  sizeof(_SimpleMethod),
  __alignof(_SimpleMethod),
  (WS_FIELD_DESCRIPTION**)&example_wsdlLocalDefinitions.globalElements.SimpleMethod._SimpleMethoddescs._SimpleMethodFields,
  WsCountOf(example_wsdlLocalDefinitions.globalElements.SimpleMethod._SimpleMethoddescs._SimpleMethodFields),
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings._SimpleMethodTypeName,
(WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.aNamespace,
  0,
  },   // struct description for _SimpleMethod
  // following are global definitions for the out parameter
  ...
  {  // element description
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings._SimpleMethodTypeName,
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.aNamespace,
  WS_STRUCT_TYPE,
  (void *)&example_wsdlLocalDefinitions.globalElements.SimpleMethod._SimpleMethoddescs.structDesc,
  },
  {    // message description for ISimpleService_SimpleMethod_InputMessage
  (WS_XML_STRING*)&example_wsdlLocalDefinitions.dictionary.xmlStrings.ISimpleService_SimpleMethod_InputMessageactionName,
(WS_ELEMENT_DESCRIPTION*)&example_wsdl.globalElements.SimpleMethod,
  },    // message description for ISimpleService_SimpleMethod_InputMessage
```

As a general rule, one level of indirection is added for all the \[out\] and \[in,out\] parameters.

## Parameterless operation

For document and literal operations, Wsutil.exe treats the operation as having one input parameter and one output parameter if:

-   The input or output message has more than one part.
-   There is only one message part and the message part name is not "parameters".

.. In the example above, assuming the message parts are named *ParamIn*" and *ParamOut*, the method signature becomes the following code:

``` syntax
typedef struct SimpleMethod{
unsigned int a;
unsigned int b;
};

typedef struct SimpleMethodResponse {
unsigned int b;
unsigned int c;
};

typedef  struct ISimpleService_SimpleMethodParamStruct
{
SimpleMethod  * SimpleMethod;
SimpleMethodResponse  * SimpleMethodResponse;
} ISimpleService_SimpleMethodParamStruct;
```

Wsutil.exe generates a version signature for the operation description such that the WsCall and server-side service model engine can check if the generated description is applicable for the current platform.

This version info is generated as part of the [**WS\_OPERATION\_DESCRIPTION**](/windows/desktop/api/WebServices/ns-webservices-ws_operation_description) structure. The version number can be treated as a union arm selector to make the structure extensible. Currently, the **versionID** is set to1 with no subsequent fields. Future versiosn may increment the version number and include more fields as needed. For example, Wsutil.exe currently generates the following code based on the version ID:

``` syntax
{ // SimpleMethod
{ // parameter descriptions for SimpleMethod
{ WS_PARAMETER_TYPE_NORMAL, (USHORT)0, (USHORT)-1 },
{ WS_PARAMETER_TYPE_NORMAL, (USHORT)1, (USHORT)-1 },
{ WS_PARAMETER_TYPE_NORMAL, (USHORT)-1, (USHORT)1 },
},    // parameter descriptions for SimpleMethod
{    // operation description for SimpleMethod
1,
(WS_MESSAGE_DESCRIPTION*)&example_wsdl.messages.ISimpleService_SimpleMethod_InputMessage,
(WS_MESSAGE_DESCRIPTION*)&example_wsdl.messages.ISimpleService_SimpleMethod_OutputMessage,
3,
(WS_PARAMETER_DESCRIPTION*)example_wsdlLocalDefinitions.contracts.DefaultBinding_ISimpleService.SimpleMethod.params,
SimpleMethodOperationStub
}, //operation description for SimpleMethod
},  // SimpleMethod
```

In the future, it could be expanded as follows:

``` syntax
WS_OPERATION_DESCRIPTION simpleMethodOperationDesc =
{
  2,
  &ISimpleService_SimpleMethod_InputputMessageDesc,
  &ISimpleService_SimpleMethod_OutputMessageDesc,
  WsCountOf(SimpleMethodParameters),
  SimpleMethodParameters,
  ISimpleService_SimpleMethod_Stub,
  &forwardToString;   // just as an example.
};
```

## Security

See the security section in the [Wsutil Compiler tool](wsutil-compiler-tool.md) topic.

 

 




