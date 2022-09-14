---
title: MetadataImportWithIssuedTokenOverSslExample
description: This example illustrates importing metadata from an endpoint that supports using an issued token that is obtained from the issuing security token service (STS) using WsRequestSecurityToken and presented to the service using WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING with WS\_SSL\_TRANSPORT\_SECURITY\_BINDING. See Federation for more information.
ms.assetid: 31d1386a-1733-4e7a-add1-9050528075c8
keywords:
- MetadataImportWithIssuedTokenOverSslExample Windows Web Services API
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# MetadataImportWithIssuedTokenOverSslExample

This example illustrates importing metadata from an endpoint that supports using an issued token that is obtained from the issuing security token service (STS) using [**WsRequestSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wsrequestsecuritytoken) and presented to the service using [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding) with [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding). See [Federation](federation.md) for more information.

## MetadataImportWithIssuedTokenOverSslExample.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include "WebServices.h"
#include "process.h"
#include "string.h"

// Print out rich error info
void PrintError(HRESULT errorCode, WS_ERROR* error)
{
    wprintf(L"Failure: errorCode=0x%lx\n", errorCode);

    if (errorCode == E_INVALIDARG || errorCode == WS_E_INVALID_OPERATION)
    {
        // Correct use of the APIs should never generate these errors
        wprintf(L"The error was due to an invalid use of an API.  This is likely due to a bug in the program.\n");
        DebugBreak();
    }

    HRESULT hr = NOERROR;
    if (error != NULL)
    {
        ULONG errorCount;
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &string);
            if (FAILED(hr))
            {
                goto Exit;
            }
            wprintf(L"%.*s\n", string.length, string.chars);
        }
    }
Exit:
    if (FAILED(hr))
    {
        wprintf(L"Could not get error string (errorCode=0x%lx)\n", hr);
    }
}

// The original URL of the WSDL document used by this example
static const WS_STRING wsdlUrl = WS_STRING_VALUE(L"http://localhost/example?wsdl");

// The WSDL document used by this example
static const WS_XML_STRING wsdlXml = WS_XML_STRING_VALUE(
"<?xml version='1.0' encoding='utf-8'?>"
"<wsdl:definitions"
"    xmlns:wsa10='http://www.w3.org/2005/08/addressing'"
"    xmlns:wsu='http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd'"
"    xmlns:wsp='http://schemas.xmlsoap.org/ws/2004/09/policy'"
"    xmlns:tns='http://example.com'"
"    xmlns:soap='http://schemas.xmlsoap.org/wsdl/soap/'"
"    xmlns:xsd='http://www.w3.org/2001/XMLSchema'"
"    xmlns:wsdl='http://schemas.xmlsoap.org/wsdl/'"
"    xmlns:wsx='http://schemas.xmlsoap.org/ws/2004/09/mex'" 
"    xmlns:wsaw='http://www.w3.org/2006/05/addressing/wsdl'" 
"    targetNamespace='http://example.com'>"
"    "
"    <wsp:Policy wsu:Id='policy'>"
"        <wsp:ExactlyOne>"
"            <wsp:All>"
"                <sp:TransportBinding xmlns:sp='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy'>"
"                  <wsp:Policy>"
"                    <sp:TransportToken>"
"                      <wsp:Policy>"
"                        <sp:HttpsToken RequireClientCertificate='false' />"
"                      </wsp:Policy>"
"                    </sp:TransportToken>"
"                    <sp:AlgorithmSuite>"
"                      <wsp:Policy>"
"                        <sp:Basic256 />"
"                      </wsp:Policy>"
"                    </sp:AlgorithmSuite>"
"                    <sp:Layout>"
"                      <wsp:Policy>"
"                        <sp:Strict />"
"                      </wsp:Policy>"
"                    </sp:Layout>"
"                    <sp:IncludeTimestamp />"
"                  </wsp:Policy>"
"                </sp:TransportBinding>"
"                <sp:EndorsingSupportingTokens xmlns:sp='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy'>"
"                  <wsp:Policy>"
"                    <sp:IssuedToken sp:IncludeToken='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy/IncludeToken/AlwaysToRecipient'>"
"                      <Issuer xmlns='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy'>"
"                        <Address xmlns='http://www.w3.org/2005/08/addressing'>http://localhost:8000/sts/x509</Address>"
"                        <Metadata xmlns='http://www.w3.org/2005/08/addressing'>"
"                          <Metadata xmlns='http://schemas.xmlsoap.org/ws/2004/09/mex' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>"
"                            <wsx:MetadataSection xmlns='>"
"                              <wsx:MetadataReference>"
"                                <Address xmlns='http://www.w3.org/2005/08/addressing'>http://localhost:8000/sts/x509/mex</Address>"
"                              </wsx:MetadataReference>"
"                            </wsx:MetadataSection>"
"                          </Metadata>"
"                        </Metadata>"
"                      </Issuer>"
"                      <sp:RequestSecurityTokenTemplate>"
"                        <t:TokenType xmlns:t='http://schemas.xmlsoap.org/ws/2005/02/trust'>http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV1.1</t:TokenType>"
"                        <t:KeyType xmlns:t='http://schemas.xmlsoap.org/ws/2005/02/trust'>http://schemas.xmlsoap.org/ws/2005/02/trust/SymmetricKey</t:KeyType>"
"                        <t:KeySize xmlns:t='http://schemas.xmlsoap.org/ws/2005/02/trust'>256</t:KeySize>"
"                        <t:Claims xmlns:t='http://schemas.xmlsoap.org/ws/2005/02/trust'>"
"                          <wsid:ClaimType Uri='http://schemas.microsoft.com/ws/2005/05/identity/claims/EmailAddress' xmlns:wsid='http://schemas.xmlsoap.org/ws/2005/05/identity' />"
"                          <wsid:ClaimType Uri='http://schemas.microsoft.com/ws/2005/05/identity/claims/UserName' Optional='true' xmlns:wsid='http://schemas.xmlsoap.org/ws/2005/05/identity' />"
"                        </t:Claims>"
"                        <MyElement />"
"                      </sp:RequestSecurityTokenTemplate>"
"                      <wsp:Policy>"
"                        <sp:RequireInternalReference />"
"                      </wsp:Policy>"
"                    </sp:IssuedToken>"
"                    <sp:SignedParts>"
"                      <sp:Header Name='To' Namespace='http://www.w3.org/2005/08/addressing' />"
"                    </sp:SignedParts>"
"                  </wsp:Policy>"
"                </sp:EndorsingSupportingTokens>"
"                <sp:Wss11 xmlns:sp='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy'>"
"                  <wsp:Policy>"
"                    <sp:MustSupportRefKeyIdentifier />"
"                    <sp:MustSupportRefIssuerSerial />"
"                    <sp:MustSupportRefThumbprint />"
"                    <sp:MustSupportRefEncryptedKey />"
"                  </wsp:Policy>"
"                </sp:Wss11>"
"                <sp:Trust10 xmlns:sp='http://schemas.xmlsoap.org/ws/2005/07/securitypolicy'>"
"                  <wsp:Policy>"
"                    <sp:MustSupportIssuedTokens />"
"                    <sp:RequireClientEntropy />"
"                    <sp:RequireServerEntropy />"
"                  </wsp:Policy>"
"                </sp:Trust10>"
"                <wsaw:UsingAddressing />"
"            </wsp:All>"
"        </wsp:ExactlyOne>"
"    </wsp:Policy>"
"    <wsdl:types>"
"        <xsd:schema targetNamespace='http://tempuri.org' xmlns:xs='http://www.w3.org/2001/XMLSchema'>"
"            <xs:element name='PingRequest'>"
"                <xs:complexType>"
"                    <xs:sequence>"
"                        <xs:element minOccurs='1' maxOccurs='1' type='xs:string'/>"
"                    </xs:sequence>"
"                </xs:complexType>"
"            </xs:element>"
"            <xs:element name='PingResponse'>"
"                <xs:complexType>"
"                    <xs:sequence>"
"                        <xs:element minOccurs='1' maxOccurs='1' type='xs:string'/>"
"                    </xs:sequence>"
"                </xs:complexType>"
"            </xs:element>"
"        </xsd:schema>"
"    </wsdl:types>"
"    <wsdl:message name='PingRequest'>"
"        <wsdl:part name='parameters' element='tns:PingRequest' />"
"    </wsdl:message>"
"    <wsdl:message name='PingResponse'>"
"        <wsdl:part name='parameters' element='tns:PingResponse' />"
"    </wsdl:message>"
"    <wsdl:message name='IPingService_echo_InputMessage'>"
"        <wsdl:part name='parameters' element='tns:echo' />"
"    </wsdl:message>"
"    <wsdl:message name='IPingService_echo_OutputMessage'>"
"        <wsdl:part name='parameters' element='tns:echoResponse' />"
"    </wsdl:message>"
"    <wsdl:binding name='Binding_IPingService' type='tns:IPingService'>"
"        <wsp:PolicyReference URI='#policy' />"
"        <soap:binding transport='http://schemas.xmlsoap.org/soap/http' />"
"        <wsdl:operation name='Ping'>"
"            <soap:operation soapAction='http://xmlsoap.org/Ping' style='document' />"
"            <wsdl:input name='PingRequest'>"
"                <soap:body use='literal' />"
"            </wsdl:input>"
"            <wsdl:output name='PingResponse'>"
"                <soap:body use='literal' />"
"            </wsdl:output>"
"        </wsdl:operation>"
"    </wsdl:binding>"
"    <wsdl:portType name='IPingService'>"
"        <wsdl:operation name='Ping'>"
"            <wsdl:input name='PingRequest' message='tns:PingRequest' />"
"            <wsdl:output name='PingResponse' message='tns:PingResponse' />"
"        </wsdl:operation>"
"    </wsdl:portType>"
"    <wsdl:service name='PingService10'>"
"        <wsdl:port name='Port_IPingService' binding='tns:Binding_IPingService'>"
"            <soap:address location='https://localhost/example' />"
"        </wsdl:port>"
"    </wsdl:service>"
"</wsdl:definitions>"
);

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_METADATA* metadata = NULL;
    WS_CHANNEL* channel = NULL;
    WS_XML_READER* reader = NULL;
    WS_HEAP* heap = NULL;
    
    // Declare constraints on what policy is acceptable
    
    // Require HTTP
    WS_CHANNEL_BINDING channelBinding = WS_HTTP_CHANNEL_BINDING;
    
    // Set up channel property contraints that override the default constraints
    WS_CHANNEL_PROPERTY_CONSTRAINT channelPropertyConstraints[3];
    
    // Allow text encodings
    WS_ENCODING allowedEncodings[] = 
    {   
        WS_ENCODING_XML_UTF8, 
        WS_ENCODING_XML_UTF16LE, 
        WS_ENCODING_XML_UTF16BE 
    }; 
    channelPropertyConstraints[0].id = WS_CHANNEL_PROPERTY_ENCODING;
    channelPropertyConstraints[0].allowedValues = allowedEncodings;
    channelPropertyConstraints[0].allowedValuesSize = sizeof(allowedEncodings);
    
    // Allow addressing 1.0
    WS_ADDRESSING_VERSION allowedAddressingVersions[] = 
    { 
        WS_ADDRESSING_VERSION_1_0,
    }; 
    channelPropertyConstraints[1].id = WS_CHANNEL_PROPERTY_ADDRESSING_VERSION;
    channelPropertyConstraints[1].allowedValues = allowedAddressingVersions;
    channelPropertyConstraints[1].allowedValuesSize = sizeof(allowedAddressingVersions);
    
    // Allow SOAP 1.1 or SOAP 1.2
    WS_ENVELOPE_VERSION allowedEnvelopeVersions[] = 
    { 
        WS_ENVELOPE_VERSION_SOAP_1_1,
        WS_ENVELOPE_VERSION_SOAP_1_2,
    }; 
    channelPropertyConstraints[2].id = WS_CHANNEL_PROPERTY_ENVELOPE_VERSION;
    channelPropertyConstraints[2].allowedValues = allowedEnvelopeVersions;
    channelPropertyConstraints[2].allowedValuesSize = sizeof(allowedEnvelopeVersions);
     
    // Set up security property contraints that override the default constraints
    WS_SECURITY_PROPERTY_CONSTRAINT securityPropertyConstraints[1];
    
    // Allow with/without a timestamp
    WS_SECURITY_TIMESTAMP_USAGE allowedTimestampValues[] = 
    {
        WS_SECURITY_TIMESTAMP_USAGE_NEVER, 
        WS_SECURITY_TIMESTAMP_USAGE_ALWAYS, 
    };
    securityPropertyConstraints[0].id = WS_SECURITY_PROPERTY_TIMESTAMP_USAGE;
    securityPropertyConstraints[0].allowedValues = allowedTimestampValues;
    securityPropertyConstraints[0].allowedValuesSize = sizeof(allowedTimestampValues);
    
    // Set up the ssl security binding constraint structure
    WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT sslSecurityBindingConstraint = { }; 
    sslSecurityBindingConstraint.bindingConstraint.type = WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE;
    
    // Set up the issued token security binding constraint structure
    WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT issuedTokenSecurityBindingConstraint = { }; 
    issuedTokenSecurityBindingConstraint.bindingConstraint.type = WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE;
    issuedTokenSecurityBindingConstraint.bindingUsage = WS_SUPPORTING_MESSAGE_SECURITY_USAGE;
    
    // Set up the set of security binding constraints
    WS_SECURITY_BINDING_CONSTRAINT* securityBindingConstraints[] =
    {
        &sslSecurityBindingConstraint.bindingConstraint,
        &issuedTokenSecurityBindingConstraint.bindingConstraint
    };
    
    // Set up the security constraint structure
    WS_SECURITY_CONSTRAINTS securityConstraints = { };
    securityConstraints.securityPropertyConstraints = securityPropertyConstraints;
    securityConstraints.securityPropertyConstraintCount = WsCountOf(securityPropertyConstraints);
    securityConstraints.securityBindingConstraints = securityBindingConstraints;
    securityConstraints.securityBindingConstraintCount = WsCountOf(securityBindingConstraints);
    
    // Set up the policy constraint structure
    WS_POLICY_CONSTRAINTS policyConstraints = { };
    policyConstraints.channelBinding = channelBinding;
    policyConstraints.channelPropertyConstraints = channelPropertyConstraints;
    policyConstraints.channelPropertyConstraintCount = WsCountOf(channelPropertyConstraints);
    policyConstraints.securityConstraints = &securityConstraints;
    
    // Set up port type to match
    static const WS_XML_STRING desiredPortTypeName = WS_XML_STRING_VALUE("IPingService");
    static const WS_XML_STRING desiredPortTypeNs = WS_XML_STRING_VALUE("http://example.com");
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create object that will hold metadata documents
    hr = WsCreateMetadata(NULL, 0, &metadata, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(
        NULL,
        0, 
        &reader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set the input of the reader to the policy text
    WS_XML_READER_BUFFER_INPUT bufferInput;
    ZeroMemory(&bufferInput, sizeof(bufferInput));
    bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    bufferInput.encodedData = wsdlXml.bytes;
    bufferInput.encodedDataSize = wsdlXml.length;
    WS_XML_READER_TEXT_ENCODING textEncoding;
    ZeroMemory(&textEncoding, sizeof(textEncoding));
    textEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
    textEncoding.charSet = WS_CHARSET_AUTO;
    hr = WsSetInput(reader, &textEncoding.encoding, &bufferInput.input, NULL, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Read the metadata into the metadata object.
    hr = WsReadMetadata(metadata, reader, &wsdlUrl, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // After adding a document to the metadata object, it can be queried
    // to determine the address of any documents which have been referenced
    // but have not yet been added.
    WS_ENDPOINT_ADDRESS* missingAddress;
    hr = WsGetMissingMetadataDocumentAddress(metadata, &missingAddress, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    if (missingAddress != NULL)
    {
        // We only support one document in this example
        hr = E_FAIL;
        goto Exit;
    }
    
    // Get the endpoints from the metadata object
    WS_METADATA_ENDPOINTS endpoints;
    hr = WsGetMetadataEndpoints(metadata, &endpoints, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    BOOL foundEndpoint = FALSE;
    WS_METADATA_ENDPOINT* endpoint = NULL;
    
    // Search for port types
    for (ULONG i = 0; i < endpoints.endpointCount; i++)
    {
        // Get the endpoint from the array of endpoints
        endpoint = &endpoints.endpoints[i];
        
        // See if the port type name matches
        hr = WsXmlStringEquals(endpoint->portTypeName, &desiredPortTypeName, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        if (hr == S_FALSE)
        {
            continue;
        }
        
        // See if the port type namespace matches
        hr = WsXmlStringEquals(endpoint->portTypeNs, &desiredPortTypeNs, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        if (hr == S_FALSE)
        {
            continue;
        }
        
        foundEndpoint = TRUE;
        break;
    }
    
    if (!foundEndpoint)
    {
        // No matching port types
        hr = E_FAIL;
        goto Exit;
    }
    
    // Get the policy for the endpoint
    WS_POLICY* policy;
    policy = endpoint->endpointPolicy;
    
    // Get the number of policy alternatives available in the policy object
    ULONG alternativeCount;
    hr = WsGetPolicyAlternativeCount(
        policy, 
        &alternativeCount, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create a heap used to allocate fields of initialized values
    hr = WsCreateHeap(/* maxSize */ 16*1024, /* trimSize */ 2*1024, NULL, 0, &heap, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    BOOL matchFound = FALSE;
    
    // For each alternative in the policy object
    for (ULONG alternativeIndex = 0; alternativeIndex < alternativeCount; alternativeIndex++)
    {
        // This example uses FALSE for the matchRequired parameter to WsMatchPolicyAlternative
        // which means that the function will return S_FALSE if there is not a match.  
        // If diagnosing why a policy cannot be matched, it may be useful to instead set
        // matchRequired to TRUE meaning an error will be returned (and the error object
        // will contain information about why the policy did not match).
        BOOL matchRequired = FALSE;
        
        // Try to match policy given the constraints
        hr = WsMatchPolicyAlternative(
            policy, 
            alternativeIndex, 
            &policyConstraints, 
            matchRequired,
            heap, 
            error);
        
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        if (hr == S_OK)
        {
            // The policy met the constraints
            matchFound = TRUE;
            break;
        }
    }
    
    if (!matchFound)
    {
        // None of the policy alternatives matched
        hr = E_FAIL;
        goto Exit;
    }
    
    // Initialize channel properties based on the values found in the policy
    WS_CHANNEL_PROPERTY channelProperties[4];
    channelProperties[0] = channelPropertyConstraints[0].out.channelProperty;
    channelProperties[1] = channelPropertyConstraints[1].out.channelProperty;
    channelProperties[2] = channelPropertyConstraints[2].out.channelProperty;
    
    // Initialize additional channel properties that specify local behavior
    // that is not part of policy.
    WS_TRANSFER_MODE transferMode = WS_BUFFERED_TRANSFER_MODE;
    channelProperties[3].id = WS_CHANNEL_PROPERTY_TRANSFER_MODE;
    channelProperties[3].value = &transferMode;
    channelProperties[3].valueSize = sizeof(transferMode);
    
    // Initialize security properties based on values extracted from policy
    WS_SECURITY_PROPERTY securityProperties[1];
    securityProperties[0] = securityPropertyConstraints[0].out.securityProperty;
    
    // Set up SSL security binding
    WS_SSL_TRANSPORT_SECURITY_BINDING sslSecurityBinding;
    ZeroMemory(&sslSecurityBinding, sizeof(sslSecurityBinding));
    sslSecurityBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE;
    if (sslSecurityBindingConstraint.out.clientCertCredentialRequired)
    {
        // Server wants a client cert, but this example does not have one
        hr = E_FAIL;
        goto Exit;
    }
    else
    {
        sslSecurityBinding.localCertCredential = NULL;
    }
    
    // Set up xml token security binding
    WS_XML_TOKEN_MESSAGE_SECURITY_BINDING xmlTokenSecurityBinding;
    ZeroMemory(&xmlTokenSecurityBinding, sizeof(xmlTokenSecurityBinding));
    xmlTokenSecurityBinding.binding.bindingType = WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE;
    xmlTokenSecurityBinding.bindingUsage = issuedTokenSecurityBindingConstraint.bindingUsage;
    
    // To obtain a security token to specify for the xmlToken field, use the following steps:
    // - If the binding to use with the issuer is not known, extract the metadata address, download
    //   the metadata and import it to determine the binding.  The WsReadEndpointAddressExtension
    //   function can be used to obtain the metadata address from the 
    //   issuedTokenSecurityBindingConstraint.out.issuerAddress field (see code below).
    // - Create a channel using WsCreateChannel that will be used to communicate with the issuing party.
    // - Open the channel to the address returned in issuedTokenSecurityBindingConstraint.out.issuerAddress.
    // - Use the issuedTokenSecurityBindingConstraint.out.requestSecurityTokenTemplate to request a security token.
    xmlTokenSecurityBinding.xmlToken = NULL; 
    
    // Extract the metadata address of the issuer that can be use to obtain metadata
    // about how to communicate with the issuer.  This step is not necessary if the protocol
    // to use with the issuer is known.  
    WS_ENDPOINT_ADDRESS* issuerMetadataAddress;
    hr = WsReadEndpointAddressExtension(
        reader,
        issuedTokenSecurityBindingConstraint.out.issuerAddress,
        WS_ENDPOINT_ADDRESS_EXTENSION_METADATA_ADDRESS,
        WS_READ_OPTIONAL_POINTER,
        heap,
        &issuerMetadataAddress,
        sizeof(issuerMetadataAddress),
        NULL);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set up security bindings
    WS_SECURITY_BINDING* securityBindings[2];
    securityBindings[0] = &sslSecurityBinding.binding;
    securityBindings[1] = &xmlTokenSecurityBinding.binding;
    
    // Set up security description
    WS_SECURITY_DESCRIPTION securityDescription;
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
    securityDescription.properties = securityProperties;
    securityDescription.propertyCount = WsCountOf(securityProperties);
    
    // Create a channel or proxy to the service using the accumulated binding information:
    // - channelBinding
    // - channelProperties
    // - securityDecription
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    
    if (metadata != NULL)
    {
        WsFreeMetadata(metadata);
    }
    if (channel != NULL)
    {
        WsFreeChannel(channel);
    }
    if (reader != NULL)
    {
        WsFreeReader(reader);
    }
    if (heap != NULL)
    {
        WsFreeHeap(heap);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}



```



## Related topics

<dl> <dt>

[**WsRequestSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wsrequestsecuritytoken)
</dt> <dt>

[**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding)
</dt> <dt>

[**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding)
</dt> <dt>

[Federation](federation.md)
</dt> </dl>

 

 




