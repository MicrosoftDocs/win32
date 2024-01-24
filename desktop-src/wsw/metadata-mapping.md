---
title: Metadata Mapping
description: The contents of a metadata document map to the metadata API in the ways explained in the following sections.
ms.assetid: 266f8319-b7ac-497f-8eb7-8e2c7bcede33
keywords:
- Metadata Mapping Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Mapping

The contents of a metadata document map to the metadata API in the ways explained in the following sections.


The following namespace prefixes are used throughout this documentation:

``` syntax
wsdl   => http://schemas.xmlsoap.org/wsdl/
soap11 => http://schemas.xmlsoap.org/wsdl/soap/
soap12 => http://schemas.xmlsoap.org/wsdl/soap12/
wsa09  => http://schemas.xmlsoap.org/ws/2004/08/addressing
wsa10  => http://www.w3.org/2005/08/addressing
wsa09p => http://schemas.xmlsoap.org/ws/2004/08/addressing/policy
wsa10p => http://www.w3.org/2006/05/addressing/wsdl
binp   => http://schemas.microsoft.com/ws/06/2004/mspolicy/netbinary1
mtomp  => http://schemas.xmlsoap.org/ws/2004/09/policy/optimizedmimeserialization
sp     => http://schemas.xmlsoap.org/ws/2005/07/securitypolicy
wsp    => http://schemas.xmlsoap.org/ws/2004/09/policy
netf   => http://schemas.microsoft.com/ws/2006/05/framing/policy
httpp  => http://schemas.microsoft.com/ws/06/2004/policy/http
wst10  => http://schemas.xmlsoap.org/ws/2005/02/trust
wsi    => http://schemas.xmlsoap.org/ws/2005/05/identity
```

The subsequent sections describe API constructs along with what metadata constructs (WSDL or Policy) they correspond to.

Familiarity with metadata specifications such as WSDL and Policy will aid in understanding this section.

## Endpoint address

The address of an endpoint (see [**WS\_ENDPOINT\_ADDRESS**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_address)) is obtained from an extensibility element within the wsdl:port element of the WSDL document. The following extensibility elements are supported for specifying the address:

``` syntax
<wsdl:port...>
    <soap11:address.../>
</wsdl:port>
```

``` syntax
<wsdl:port...>
    <soap12:address.../>
</wsdl:port>
```

``` syntax
<wsdl:port...>
    <wsa09:EndpointReference.../>
</wsdl:port>
```

``` syntax
<wsdl:port...>
    <wsa10:EndpointReference.../>
</wsdl:port>
```

## WS\_CHANNEL\_BINDING

The channel binding (see [**WS\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding)) is determined by the transport the soap binding used, as follows:

``` syntax
<soap:binding transport=&quot;http://schemas.microsoft.com/soap/tcp&quot;/> => WS_TCP_CHANNEL_BINDING
```

``` syntax
<soap:binding transport=&quot;http://schemas.xmlsoap.org/soap/http&quot;/> => WS_HTTP_CHANNEL_BINDING
```

## WS\_CHANNEL\_PROPERTY\_ENVELOPE\_VERSION

The envelope version (see [**WS\_CHANNEL\_PROPERTY\_ENVELOPE\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id)) is determined by which soap binding is used, as follows:

``` syntax
<wsdl:binding...>
    <soap11:binding.../> => WS_ENVELOPE_VERSION_SOAP_1_1
</wsdl:binding>
```

``` syntax
<wsdl:binding...>
    <soap12:binding.../> => WS_ENVELOPE_VERSION_SOAP_1_2
</wsdl:binding>
```

## Addressing Version

The addressing version (see [**WS\_CHANNEL\_PROPERTY\_ADDRESSING\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id)) is determined by the following assertions in the endpoint policy:

``` syntax
<wsp:Policy...>
    <wsa09p:UsingAddressing.../> => WS_ADDRESSING_VERSION_0_9
</wsp:Policy>
```

``` syntax
<wsp:Policy...>
    <wsa10p:UsingAddressing.../> => WS_ADDRESSING_VERSION_1_0
</wsp:Policy>
```

If an addressing assertion is not present, then [**WS\_ADDRESSING\_VERSION\_TRANSPORT**](/windows/desktop/api/WebServices/ne-webservices-ws_addressing_version) is assumed.

## Message Encoding

The encoding of the message (see [**WS\_CHANNEL\_PROPERTY\_ENCODING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_property_id)) is determined by the following assertions in the endpoint policy:

``` syntax
<wsp:Policy...>
    <binp:BinaryEncoding.../> => WS_ENCODING_XML_BINARY_SESSION_1, WS_ENCODING_XML_BINARY_1
</wsp:Policy>
```

Note that the binary encoding policy assertion does not include information about whether the binary encoding is sessionful or sessionless. This is determined by the encoding property constraint (which should be appropriate according to whether or not the [**WS\_CHANNEL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_type) being used is sessionful or not).

``` syntax
<wsp:Policy...>
    <mtomp:OptimizedMimeSerialization.../> => WS_ENCODING_XML_MTOM_UTF8, WS_ENCODING_XML_MTOM_UTF16LE, WS_ENCODING_XML_MTOM_UTF16BE
</wsp:Policy>
```

If neither of the above assertions are present, then a text encoding is used: [**WS\_ENCODING\_XML\_UTF8**](/windows/desktop/api/WebServices/ne-webservices-ws_encoding), **WS\_ENCODING\_XML\_UTF16LE**, **WS\_ENCODING\_XML\_UTF16BE**.

Note that policy does not include information about the character set for MTOM or text encodings (whether it is UTF8, UTF16LE or UTF16BE). The actual character set value used is determined by the encoding property constraint.

## Constraints with HTTP Header Authentication

This section applies when the [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding_constraint) security binding constraint is specified.

This security binding is indicated in the policy by different assertions that states both that HTTP header authentication should be used, and that a particular authentication scheme should be used. The policy assertions correspond to the values of the [**WS\_SECURITY\_BINDING\_PROPERTY\_HTTP\_HEADER\_AUTH\_SCHEME**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_property_id) as follows:

``` syntax
<wsp:Policy...>
    <httpp:BasicAuthentication.../> => WS_HTTP_HEADER_AUTH_SCHEME_BASIC
</wsp:Policy>
```

``` syntax
<wsp:Policy...>
    <httpp:NegotiateAuthentication.../> => WS_HTTP_HEADER_AUTH_SCHEME_NEGOTIATE
</wsp:Policy>
```

``` syntax
<wsp:Policy...>
    <httpp:NtlmAuthentication.../> => WS_HTTP_HEADER_AUTH_SCHEME_NTLM
</wsp:Policy>
```

``` syntax
<wsp:Policy...>
    <httpp:DigestAuthentication.../> => WS_HTTP_HEADER_AUTH_SCHEME_DIGEST
</wsp:Policy>
```

## Constraints with SLL Transport Security

This section applies when the [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<wsp:Policy...>
    <sp:TransportBinding...>
        <wsp:Policy...>
            <sp:TransportToken...>
                <wsp:Policy...>
                    <sp:HttpsToken.../>
            </wsp:Policy...>
        </wsp:Policy>
    </sp:TransportBinding...>
</wsp:Policy>
```

## Constraints with SSPI Transport Security

This section applies when the [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<wsp:Policy...>
    <sp:TransportBinding...>
        <wsp:Policy...>
            <sp:TransportToken...>
                <wsp:Policy...>
                    <netf:WindowsTransportSecurity.../>
            </wsp:Policy...>
        </wsp:Policy>
    </sp:TransportBinding...>
</wsp:Policy>
```

## Constrains with Transport Security

The [**WS\_SECURITY\_PROPERTY\_TRANSPORT\_PROTECTION\_LEVEL**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id) property constraint can be specified if any of the security binding constraints are specified:

-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding_constraint)

    The value from policy is always [**WS\_PROTECTION\_LEVEL\_SIGN\_AND\_ENCRYPT**](/windows/desktop/api/WebServices/ne-webservices-ws_protection_level).

-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding_constraint)

    The value from policy is specified as part of the WindowsTransportSecurity assertion, as follows:

    ``` syntax
    <netf:WindowsTransportSecurity...>None</netf:WindowsTransportSecurity> => WS_PROTECTION_LEVEL_NONE
    ```

    ``` syntax
    <netf:WindowsTransportSecurity...>Sign</netf:WindowsTransportSecurity> => WS_PROTECTION_LEVEL_SIGN
    ```

    ``` syntax
    <netf:WindowsTransportSecurity...>EncryptAndSign</netf:WindowsTransportSecurity> => WS_PROTECTION_LEVEL_SIGN_AND_ENCRYPT
    ```

-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding_constraint)

    The value from policy is always [**WS\_PROTECTION\_LEVEL\_NONE**](/windows/desktop/api/WebServices/ne-webservices-ws_protection_level).

## Constraints with Kerberos APREQ Security Binding

This section applies when the [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<sp:EndorsingSupportingTokens...>
    <wsp:Policy>
        <sp:KerberosToken>
            <WssGssKerberosV5ApReqToken11.../>
        </sp:KerberosToken>
    </wsp:Policy>
</sp:EndorsingSupportingTokens>
```

## Constraints with Message Security Binding

This section applies when the [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<sp:SignedSupportingTokens>
    <wsp:Policy>
        <sp:UsernameToken.../>
    </wsp:Policy>
</sp:SignedSupportingTokens>
```

## WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT

This section applies when the [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<sp:EndorsingSupportingTokens>
    <wsp:Policy>
        <sp:X509Token.../>
   </wsp:Policy>
</sp:EndorsingSupportingTokens>
```

## WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT

This section applies when the [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<sp:EndorsingSupportingTokens...>
    <wsp:Policy>
        <sp:IssuedToken sp:IncludeToken=&quot;xs:anyURI&quot;? ...=&quot;&quot; >
            <wsp:Issuer>...</wsp:Issuer>?
            <wsp:RequestSecurityTokenTemplate TrustVersion='xs:anyURI&quot;?>
                ...
                <wst10:Claims>
                    <wsi:ClaimType Optional='xs:boolean'?>xs:anyURI<wt:ClaimType>*
                </wst10:Claims>
                ...
            </wsp:RequestSecurityTokenTemplate>
            <wsp:Policy>
                <sp:RequireDerivedKeys/> ?
                <sp:RequireExternalReference/> ?
                <sp:RequireInternalReference/> ?
            </wsp:Policy> ?
        </sp:IssuedToken>
    </wsp:Policy>
</sp:EndorsingSupportingTokens>
```

The following describes the mapping of fields of the [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint) to the above policy:

-   The claimConstraints field is used to verify the set of claim type URIs that appear within the wsi:ClaimType element above.

-   The issuerAddress field corresponds to the wsp:Issuer element above, which is the [**WS\_ENDPOINT\_ADDRESS**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_address) of the service that can issue the token.

-   The requestSecurityTokenTemplate field corresponds to the child elements of the wsp:RequestSecurityTokenTemplate element.

## WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT

This section applies when the [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used in this case:

``` syntax
<sp:EndorsingSupportingTokens...>
    <wsp:Policy>
        <sp:SecureConversationToken sp:IncludeToken=&quot;xs:anyURI&quot;? ...=&quot;&quot; >
            <wsp:Issuer>...</wsp:Issuer>?
            <wsp:Policy>
                <sp:RequireDerivedKeys.../>?
                <sp:RequireExternalUriReference.../>?
                <sp:SC10SecurityContextToken.../>? => WS_SECURE_CONVERSATION_VERSION_FEBRUARY_2005
                <sp:BootstrapPolicy... >?
                   <wsp:Policy> ...  </wsp:Policy> => WS_SECURITY_CONSTRAINTS
                </sp:BootstrapPolicy>
            </wsp:Policy>
        </wsp:SecureConversationToken>
    </wsp:Policy>
</sp:EndorsingSupportingTokens>
```

The entropy mode is determined by the <sp:Trust10> assertion. <sp:RequireClientEntropy/> and <sp:RequireServerEntropy/> => [**WS\_SECURITY\_KEY\_ENTROPY\_MODE\_COMBINED**](/windows/desktop/api/WebServices/ne-webservices-ws_security_key_entropy_mode) <sp:RequireClientEntropy/> => **WS\_SECURITY\_KEY\_ENTROPY\_MODE\_CLIENT\_ONLY** <sp:RequireServerEntropy/> => **WS\_SECURITY\_KEY\_ENTROPY\_MODE\_SERVER\_ONLY**

## WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_TRUST\_VERSION

This section applies when the [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint) security binding constraint is specified. The following policy assertions are used to identify the [**WS\_TRUST\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_trust_version) and associated options.

``` syntax
<sp:Trust10> => WS_TRUST_VERSION_FEBRUARY_2005
    <sp:Policy>
        <sp:MustSupportClientChallenge/> ?
        <sp:MustSupportServerChallenge/> ?
        <sp:RequireClientEntropy/> ?
        <sp:RequireServerEntropy/> ?
        <sp:MustSupportIssuedTokens/> ?
    </sp:Policy>
</sp:Trust10>
```

The trust version can be specified using the [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_request_security_token_property_constraint) with a property id of [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_TRUST\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_request_security_token_property_id).

## WS\_SECURITY\_PROPERTY\_SECURITY\_HEADER\_VERSION

This section applies when any of the following binding constraints are used:

-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding_constraint)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding_constraint)
-   [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_message_security_binding_constraint)
-   [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint)

The header security version (as specified by [**WS\_SECURITY\_PROPERTY\_SECURITY\_HEADER\_VERSION**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)) is determined by one of the following policy assertions:

``` syntax
<wsp:Wss10> ... </wsp:Wss10> => WS_SECURITY_HEADER_VERSION_1_0
```

``` syntax
<wsp:Wss11> ... </wsp:Wss11> => WS_SECURITY_HEADER_VERSION_1_1
```

## Constraints with Header Security Layout

This section applies when any of the following binding constraints are used:

-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding_constraint)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding_constraint)
-   [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_message_security_binding_constraint)
-   [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint)

The security header layout (as specified by [**WS\_SECURITY\_PROPERTY\_SECURITY\_HEADER\_LAYOUT**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)) is determined by one of the following policy assertions:

``` syntax
<sp:TransportBinding>
    <wsp:Policy>
        <sp:Layout>
            <sp:Lax.../> => WS_SECURITY_HEADER_LAYOUT_LAX
        </sp:Layout>
    </wsp:Policy>
</sp:TransportBinding>
```

``` syntax
<sp:TransportBinding>
    <wsp:Policy>
        <sp:Layout>
            <sp:Strict.../> => WS_SECURITY_HEADER_LAYOUT_STRICT
        </sp:Layout>
    </wsp:Policy>
</sp:TransportBinding>
```

``` syntax
<sp:TransportBinding>
    <wsp:Policy>
        <sp:Layout>
            <sp:LaxTsFirst.../> => WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_FIRST
        </sp:Layout>
    </wsp:Policy>
</sp:TransportBinding>
```

``` syntax
<sp:TransportBinding>
    <wsp:Policy>
        <sp:Layout>
            <sp:LaxTsLast.../> => WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_LAST
        </sp:Layout>
    </wsp:Policy>
</sp:TransportBinding>
```

## Constraints with Timestamp Security

This section applies when any of the following binding constraints are used:

-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding_constraint)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding_constraint)
-   [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_message_security_binding_constraint)
-   [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint)

Whether or not a timestamp is included in the security header (as specified by [**WS\_SECURITY\_PROPERTY\_TIMESTAMP\_USAGE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)) is determined by the presence of the sp:IncludeTimestamp in the following location:

``` syntax
<sp:TransportBinding>
    <wsp:Policy>
        <sp:IncludeTimestamp.../>
    </wsp:Policy>
</sp:TransportBinding>
```

If the sp:IncludeTimestamp assertion is present, the value from policy is [**WS\_SECURITY\_TIMESTAMP\_USAGE\_ALWAYS**](/windows/desktop/api/WebServices/ne-webservices-ws_security_timestamp_usage).

If the sp:IncludeTimestamp assertion is not present, the value from policy is [**WS\_SECURITY\_TIMESTAMP\_USAGE\_NEVER**](/windows/desktop/api/WebServices/ne-webservices-ws_security_timestamp_usage).

 

 




