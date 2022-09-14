---
title: AsmxTerraServiceSampleWithCustomProxy
description: This examples shows service proxy talking to a ASMX TerraService service using WS\_HTTP\_PROXY\_SETTING\_MODE\_CUSTOM channel property.
ms.assetid: 200dfcbc-ad16-4ac8-ab16-76291344a980
keywords:
- AsmxTerraServiceSampleWithCustomProxy Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# AsmxTerraServiceSampleWithCustomProxy

This examples shows service proxy talking to a ASMX TerraService service using [**WS\_HTTP\_PROXY\_SETTING\_MODE\_CUSTOM**](/windows/desktop/api/WebServices/ne-webservices-ws_http_proxy_setting_mode) channel property.

-   [AsmxCustomProxyClient.cpp](#asmxcustomproxyclientcpp)
-   [terraserviceusa.com.wsdl](#terraserviceusacomwsdl)
-   [Related topics](#related-topics)

## AsmxCustomProxyClient.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#include "windows.h"
#include "winhttp.h"
#ifndef UNICODE
#define UNICODE
#endif
#include "WebServices.h"
#include "process.h"
#include "stdio.h"
#include "string.h"
#include "terraserviceusa.com.wsdl.h"

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


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_SERVICE_PROXY* serviceProxy = NULL;
    WS_HEAP* heap = NULL;
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING serviceUrl = WS_STRING_VALUE(L"https://terraservice.net/TerraService2.asmx");
    WS_CHANNEL_PROPERTY channelPropertyArray[4];
    WS_ADDRESSING_VERSION addressingVersion = WS_ADDRESSING_VERSION_TRANSPORT;
    WS_ENVELOPE_VERSION envelopeVersion = WS_ENVELOPE_VERSION_SOAP_1_1;
    WS_STRING place = WS_STRING_VALUE(L"");
    WS_HTTP_PROXY_SETTING_MODE proxySettingMode = WS_HTTP_PROXY_SETTING_MODE_CUSTOM;
    WS_CUSTOM_HTTP_PROXY customProxy = {};
    address.url = serviceUrl;
    WINHTTP_AUTOPROXY_OPTIONS autoProxyOptions = {};
    WINHTTP_PROXY_INFO proxyInfo = {};
    HINTERNET session = NULL;
    
    channelPropertyArray[0].id = WS_CHANNEL_PROPERTY_ADDRESSING_VERSION;
    channelPropertyArray[0].value = &addressingVersion;
    channelPropertyArray[0].valueSize = sizeof(addressingVersion);
    
    channelPropertyArray[1].id = WS_CHANNEL_PROPERTY_ENVELOPE_VERSION;
    channelPropertyArray[1].value = &envelopeVersion;
    channelPropertyArray[1].valueSize = sizeof(envelopeVersion);
    
    channelPropertyArray[2].id = WS_CHANNEL_PROPERTY_HTTP_PROXY_SETTING_MODE;
    channelPropertyArray[2].value = &proxySettingMode;
    channelPropertyArray[2].valueSize = sizeof(proxySettingMode);
    
    channelPropertyArray[3].id = WS_CHANNEL_PROPERTY_CUSTOM_HTTP_PROXY;
    channelPropertyArray[3].value = &customProxy;
    channelPropertyArray[3].valueSize = sizeof(customProxy);
    
    
    // This part illustrates how to setup a HTTP header authentication security binding
    // against the HTTP proxy server in case it requires authentication.
    // declare and initialize a default windows credential
    WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL windowsCredential = {}; // zero out the struct
    windowsCredential.credential.credentialType = WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE; // set the credential type
    // for illustration only; usernames and passwords should never be included in source files
    windowsCredential.username.chars = L"domain\\user";
    windowsCredential.username.length = (ULONG)wcslen(windowsCredential.username.chars);
    windowsCredential.password.chars = L"password";
    windowsCredential.password.length = (ULONG)wcslen(windowsCredential.password.chars);
    
    // declare and initialize properties to set the authentication scheme to Basic
    ULONG scheme = WS_HTTP_HEADER_AUTH_SCHEME_NEGOTIATE;
    ULONG target = WS_HTTP_HEADER_AUTH_TARGET_PROXY;
    WS_SECURITY_BINDING_PROPERTY httpProxyAuthBindingProperties[2] =
    {
        { WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_SCHEME, &scheme, sizeof(scheme) },
        { WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_TARGET, &target, sizeof(target) }
    };
    
    // declare and initialize an HTTP header authentication security binding for the HTTP proxy server
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING httpProxyAuthBinding = {}; // zero out the struct
    httpProxyAuthBinding.binding.bindingType = WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TYPE; // set the binding type
    httpProxyAuthBinding.binding.properties = httpProxyAuthBindingProperties;
    httpProxyAuthBinding.binding.propertyCount = WsCountOf(httpProxyAuthBindingProperties);
    httpProxyAuthBinding.clientCredential = &windowsCredential.credential;
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[1] = { &httpProxyAuthBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create a heap to store deserialized data
    hr = WsCreateHeap(
        /*maxSize*/ 2048, 
        /*trimSize*/ 512, 
        NULL, 
        0, 
        &heap, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    session = WinHttpOpen(L"NWS Example",
        WINHTTP_ACCESS_TYPE_NO_PROXY, 
        WINHTTP_NO_PROXY_NAME,
        WINHTTP_NO_PROXY_BYPASS,
        WINHTTP_FLAG_ASYNC);
    if (!session)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    autoProxyOptions.dwFlags = WINHTTP_AUTOPROXY_RUN_INPROCESS | WINHTTP_AUTOPROXY_AUTO_DETECT;
    autoProxyOptions.dwAutoDetectFlags = WINHTTP_AUTO_DETECT_TYPE_DHCP | WINHTTP_AUTO_DETECT_TYPE_DNS_A;
    autoProxyOptions.fAutoLogonIfChallenged = FALSE;
    
    WinHttpGetProxyForUrl(
        session,
        serviceUrl.chars,
        &autoProxyOptions,
        &proxyInfo);
    
    if (proxyInfo.dwAccessType == WINHTTP_ACCESS_TYPE_NAMED_PROXY)
    {
        if (proxyInfo.lpszProxy)
        {
            customProxy.servers.chars = proxyInfo.lpszProxy;
            customProxy.servers.length = (ULONG)wcslen(proxyInfo.lpszProxy);
        }
        if (proxyInfo.lpszProxyBypass)
        {
            customProxy.bypass.chars = proxyInfo.lpszProxyBypass;
            customProxy.bypass.length = (ULONG)wcslen(proxyInfo.lpszProxyBypass);
        }
    }
    
    hr = WsCreateServiceProxy(
            WS_CHANNEL_TYPE_REQUEST, 
            WS_HTTP_CHANNEL_BINDING, 
            &securityDescription, 
            NULL, 
            0,
            channelPropertyArray,
            WsCountOf(channelPropertyArray),
            &serviceProxy, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    // Open channel to address
    hr = WsOpenServiceProxy(
            serviceProxy, 
            &address, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    for (int i = 0; i < 100; i++)
    {
        LonLatPt point = {10.0, 10.0};
        hr = TerraServiceSoap_ConvertLonLatPtToNearestPlace(
            serviceProxy,
            &point,
            &place,
            heap,
            NULL,
            0,
            NULL,
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        wprintf(L"Place @ Lattitude=%f, Longitutde=%f is %s\n", 
            point.Lon,
            point.Lat,
            place);
        fflush(stdout);
        hr = WsResetHeap(
            heap,
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    if (proxyInfo.lpszProxy)
    {
        ::GlobalFree(proxyInfo.lpszProxy);
    }
    if (proxyInfo.lpszProxyBypass)
    {
        ::GlobalFree(proxyInfo.lpszProxyBypass);
    }
    if (serviceProxy != NULL)
    {
        WsCloseServiceProxy(serviceProxy, NULL, NULL);
        WsFreeServiceProxy(serviceProxy);
    }
    if (!session)
    {
        WinHttpCloseHandle(session);
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



## terraserviceusa.com.wsdl

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="https://microsoft.com/wsdl/mime/textMatching/" xmlns:soapenc="https://schemas.xmlsoap.org/soap/encoding/" xmlns:mime="https://schemas.xmlsoap.org/wsdl/mime/" xmlns:tns="https://terraservice-usa.com/" xmlns:s="https://www.w3.org/2001/XMLSchema" xmlns:http="https://schemas.xmlsoap.org/wsdl/http/" targetNamespace="https://terraservice-usa.com/" xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <s:schema elementFormDefault="qualified" targetNamespace="https://terraservice-usa.com/">
      <s:element name="ConvertLonLatPtToNearestPlace">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="point" type="tns:LonLatPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="LonLatPt">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Lon" type="s:double" />
          <s:element minOccurs="1" maxOccurs="1" name="Lat" type="s:double" />
        </s:sequence>
      </s:complexType>
      <s:element name="ConvertLonLatPtToNearestPlaceResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="ConvertLonLatPtToNearestPlaceResult" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="ConvertLonLatPtToUtmPt">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="point" type="tns:LonLatPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="ConvertLonLatPtToUtmPtResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="ConvertLonLatPtToUtmPtResult" type="tns:UtmPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="UtmPt">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Zone" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="X" type="s:double" />
          <s:element minOccurs="1" maxOccurs="1" name="Y" type="s:double" />
        </s:sequence>
      </s:complexType>
      <s:element name="ConvertUtmPtToLonLatPt">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="utm" type="tns:UtmPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="ConvertUtmPtToLonLatPtResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="ConvertUtmPtToLonLatPtResult" type="tns:LonLatPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="ConvertPlaceToLonLatPt">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="place" type="tns:Place" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="Place">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="1" name="City" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="State" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="Country" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:element name="ConvertPlaceToLonLatPtResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="ConvertPlaceToLonLatPtResult" type="tns:LonLatPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="CountPlacesInRect">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="upperleft" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="lowerright" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="ptype" type="tns:PlaceType" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:simpleType name="PlaceType">
        <s:restriction base="s:string">
          <s:enumeration value="UnknownPlaceType" />
          <s:enumeration value="AirRailStation" />
          <s:enumeration value="BayGulf" />
          <s:enumeration value="CapePeninsula" />
          <s:enumeration value="CityTown" />
          <s:enumeration value="HillMountain" />
          <s:enumeration value="Island" />
          <s:enumeration value="Lake" />
          <s:enumeration value="OtherLandFeature" />
          <s:enumeration value="OtherWaterFeature" />
          <s:enumeration value="ParkBeach" />
          <s:enumeration value="PointOfInterest" />
          <s:enumeration value="River" />
        </s:restriction>
      </s:simpleType>
      <s:element name="CountPlacesInRectResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="CountPlacesInRectResult" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAreaFromPt">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="center" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="theme" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="scale" type="tns:Scale" />
            <s:element minOccurs="1" maxOccurs="1" name="displayPixWidth" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="displayPixHeight" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:simpleType name="Scale">
        <s:restriction base="s:string">
          <s:enumeration value="Scale1mm" />
          <s:enumeration value="Scale2mm" />
          <s:enumeration value="Scale4mm" />
          <s:enumeration value="Scale8mm" />
          <s:enumeration value="Scale16mm" />
          <s:enumeration value="Scale32mm" />
          <s:enumeration value="Scale63mm" />
          <s:enumeration value="Scale125mm" />
          <s:enumeration value="Scale250mm" />
          <s:enumeration value="Scale500mm" />
          <s:enumeration value="Scale1m" />
          <s:enumeration value="Scale2m" />
          <s:enumeration value="Scale4m" />
          <s:enumeration value="Scale8m" />
          <s:enumeration value="Scale16m" />
          <s:enumeration value="Scale32m" />
          <s:enumeration value="Scale64m" />
          <s:enumeration value="Scale128m" />
          <s:enumeration value="Scale256m" />
          <s:enumeration value="Scale512m" />
          <s:enumeration value="Scale1km" />
          <s:enumeration value="Scale2km" />
          <s:enumeration value="Scale4km" />
          <s:enumeration value="Scale8km" />
          <s:enumeration value="Scale16km" />
          <s:enumeration value="Scale32km" />
          <s:enumeration value="Scale64km" />
          <s:enumeration value="Scale128km" />
          <s:enumeration value="Scale256km" />
          <s:enumeration value="Scale512km" />
          <s:enumeration value="Scale1024km" />
          <s:enumeration value="Scale2048km" />
        </s:restriction>
      </s:simpleType>
      <s:element name="GetAreaFromPtResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetAreaFromPtResult" type="tns:AreaBoundingBox" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="AreaBoundingBox">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="NorthWest" type="tns:AreaCoordinate" />
          <s:element minOccurs="1" maxOccurs="1" name="NorthEast" type="tns:AreaCoordinate" />
          <s:element minOccurs="1" maxOccurs="1" name="SouthWest" type="tns:AreaCoordinate" />
          <s:element minOccurs="1" maxOccurs="1" name="SouthEast" type="tns:AreaCoordinate" />
          <s:element minOccurs="1" maxOccurs="1" name="Center" type="tns:AreaCoordinate" />
          <s:element minOccurs="0" maxOccurs="1" name="NearestPlace" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="OverlappingThemeInfos" type="tns:ArrayOfOverlappingThemeInfo" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="AreaCoordinate">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="TileMeta" type="tns:TileMeta" />
          <s:element minOccurs="1" maxOccurs="1" name="Offset" type="tns:LonLatPtOffset" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="TileMeta">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Id" type="tns:TileId" />
          <s:element minOccurs="1" maxOccurs="1" name="TileExists" type="s:boolean" />
          <s:element minOccurs="1" maxOccurs="1" name="NorthWest" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="NorthEast" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="SouthWest" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="SouthEast" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="Center" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="Capture" type="s:dateTime" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="TileId">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Theme" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="Scale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="Scene" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="X" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="Y" type="s:int" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="LonLatPtOffset">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Point" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="XOffset" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="YOffset" type="s:int" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="ArrayOfOverlappingThemeInfo">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="OverlappingThemeInfo" type="tns:OverlappingThemeInfo" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="OverlappingThemeInfo">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="LocalTheme" type="s:boolean" />
          <s:element minOccurs="1" maxOccurs="1" name="Theme" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="Point" type="tns:LonLatPt" />
          <s:element minOccurs="0" maxOccurs="1" name="ThemeName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="Capture" type="s:dateTime" />
          <s:element minOccurs="1" maxOccurs="1" name="ProjectionId" type="tns:ProjectionType" />
          <s:element minOccurs="1" maxOccurs="1" name="LoScale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="HiScale" type="tns:Scale" />
          <s:element minOccurs="0" maxOccurs="1" name="Url" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:simpleType name="ProjectionType">
        <s:restriction base="s:string">
          <s:enumeration value="Geographic" />
          <s:enumeration value="UtmNad27" />
          <s:enumeration value="UtmNad83" />
        </s:restriction>
      </s:simpleType>
      <s:element name="GetAreaFromRect">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="upperLeft" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="lowerRight" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="theme" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="scale" type="tns:Scale" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAreaFromRectResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetAreaFromRectResult" type="tns:AreaBoundingBox" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAreaFromTileId">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="id" type="tns:TileId" />
            <s:element minOccurs="1" maxOccurs="1" name="displayPixWidth" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="displayPixHeight" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetAreaFromTileIdResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetAreaFromTileIdResult" type="tns:AreaBoundingBox" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetLatLonMetrics">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="point" type="tns:LonLatPt" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetLatLonMetricsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetLatLonMetricsResult" type="tns:ArrayOfThemeBoundingBox" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="ArrayOfThemeBoundingBox">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="ThemeBoundingBox" type="tns:ThemeBoundingBox" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="ThemeBoundingBox">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Theme" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="ThemeName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="Sparseness" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="LoScale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="HiScale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="ProjectionId" type="tns:ProjectionType" />
          <s:element minOccurs="0" maxOccurs="1" name="ProjectionName" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="WestLongitude" type="s:double" />
          <s:element minOccurs="1" maxOccurs="1" name="NorthLatitude" type="s:double" />
          <s:element minOccurs="1" maxOccurs="1" name="EastLongitude" type="s:double" />
          <s:element minOccurs="1" maxOccurs="1" name="SouthLatitude" type="s:double" />
        </s:sequence>
      </s:complexType>
      <s:element name="GetPlaceFacts">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="place" type="tns:Place" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetPlaceFactsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetPlaceFactsResult" type="tns:PlaceFacts" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="PlaceFacts">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Place" type="tns:Place" />
          <s:element minOccurs="1" maxOccurs="1" name="Center" type="tns:LonLatPt" />
          <s:element minOccurs="1" maxOccurs="1" name="AvailableThemeMask" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="PlaceTypeId" type="tns:PlaceType" />
          <s:element minOccurs="1" maxOccurs="1" name="Population" type="s:int" />
        </s:sequence>
      </s:complexType>
      <s:element name="GetPlaceList">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="placeName" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="MaxItems" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="imagePresence" type="s:boolean" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetPlaceListResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetPlaceListResult" type="tns:ArrayOfPlaceFacts" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="ArrayOfPlaceFacts">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="PlaceFacts" type="tns:PlaceFacts" />
        </s:sequence>
      </s:complexType>
      <s:element name="GetPlaceListInRect">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="upperleft" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="lowerright" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="ptype" type="tns:PlaceType" />
            <s:element minOccurs="1" maxOccurs="1" name="MaxItems" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetPlaceListInRectResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetPlaceListInRectResult" type="tns:ArrayOfPlaceFacts" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTheme">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="theme" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetThemeResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetThemeResult" type="tns:ThemeInfo" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="ThemeInfo">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="Theme" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="Name" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="Description" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="Supplier" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="LoScale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="HiScale" type="tns:Scale" />
          <s:element minOccurs="1" maxOccurs="1" name="ProjectionId" type="tns:ProjectionType" />
          <s:element minOccurs="0" maxOccurs="1" name="ProjectionName" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="CopyrightNotice" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:element name="GetTileMetaFromLonLatPt">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="point" type="tns:LonLatPt" />
            <s:element minOccurs="1" maxOccurs="1" name="theme" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="scale" type="tns:Scale" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTileMetaFromLonLatPtResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetTileMetaFromLonLatPtResult" type="tns:TileMeta" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTileMetaFromTileId">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="id" type="tns:TileId" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTileMetaFromTileIdResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="GetTileMetaFromTileIdResult" type="tns:TileMeta" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTile">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="id" type="tns:TileId" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="GetTileResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="GetTileResult" type="s:base64Binary" />
          </s:sequence>
        </s:complexType>
      </s:element>
    </s:schema>
  </wsdl:types>
  <wsdl:message name="ConvertLonLatPtToNearestPlaceSoapIn">
    <wsdl:part name="parameters" element="tns:ConvertLonLatPtToNearestPlace" />
  </wsdl:message>
  <wsdl:message name="ConvertLonLatPtToNearestPlaceSoapOut">
    <wsdl:part name="parameters" element="tns:ConvertLonLatPtToNearestPlaceResponse" />
  </wsdl:message>
  <wsdl:message name="ConvertLonLatPtToUtmPtSoapIn">
    <wsdl:part name="parameters" element="tns:ConvertLonLatPtToUtmPt" />
  </wsdl:message>
  <wsdl:message name="ConvertLonLatPtToUtmPtSoapOut">
    <wsdl:part name="parameters" element="tns:ConvertLonLatPtToUtmPtResponse" />
  </wsdl:message>
  <wsdl:message name="ConvertUtmPtToLonLatPtSoapIn">
    <wsdl:part name="parameters" element="tns:ConvertUtmPtToLonLatPt" />
  </wsdl:message>
  <wsdl:message name="ConvertUtmPtToLonLatPtSoapOut">
    <wsdl:part name="parameters" element="tns:ConvertUtmPtToLonLatPtResponse" />
  </wsdl:message>
  <wsdl:message name="ConvertPlaceToLonLatPtSoapIn">
    <wsdl:part name="parameters" element="tns:ConvertPlaceToLonLatPt" />
  </wsdl:message>
  <wsdl:message name="ConvertPlaceToLonLatPtSoapOut">
    <wsdl:part name="parameters" element="tns:ConvertPlaceToLonLatPtResponse" />
  </wsdl:message>
  <wsdl:message name="CountPlacesInRectSoapIn">
    <wsdl:part name="parameters" element="tns:CountPlacesInRect" />
  </wsdl:message>
  <wsdl:message name="CountPlacesInRectSoapOut">
    <wsdl:part name="parameters" element="tns:CountPlacesInRectResponse" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromPtSoapIn">
    <wsdl:part name="parameters" element="tns:GetAreaFromPt" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromPtSoapOut">
    <wsdl:part name="parameters" element="tns:GetAreaFromPtResponse" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromRectSoapIn">
    <wsdl:part name="parameters" element="tns:GetAreaFromRect" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromRectSoapOut">
    <wsdl:part name="parameters" element="tns:GetAreaFromRectResponse" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromTileIdSoapIn">
    <wsdl:part name="parameters" element="tns:GetAreaFromTileId" />
  </wsdl:message>
  <wsdl:message name="GetAreaFromTileIdSoapOut">
    <wsdl:part name="parameters" element="tns:GetAreaFromTileIdResponse" />
  </wsdl:message>
  <wsdl:message name="GetLatLonMetricsSoapIn">
    <wsdl:part name="parameters" element="tns:GetLatLonMetrics" />
  </wsdl:message>
  <wsdl:message name="GetLatLonMetricsSoapOut">
    <wsdl:part name="parameters" element="tns:GetLatLonMetricsResponse" />
  </wsdl:message>
  <wsdl:message name="GetPlaceFactsSoapIn">
    <wsdl:part name="parameters" element="tns:GetPlaceFacts" />
  </wsdl:message>
  <wsdl:message name="GetPlaceFactsSoapOut">
    <wsdl:part name="parameters" element="tns:GetPlaceFactsResponse" />
  </wsdl:message>
  <wsdl:message name="GetPlaceListSoapIn">
    <wsdl:part name="parameters" element="tns:GetPlaceList" />
  </wsdl:message>
  <wsdl:message name="GetPlaceListSoapOut">
    <wsdl:part name="parameters" element="tns:GetPlaceListResponse" />
  </wsdl:message>
  <wsdl:message name="GetPlaceListInRectSoapIn">
    <wsdl:part name="parameters" element="tns:GetPlaceListInRect" />
  </wsdl:message>
  <wsdl:message name="GetPlaceListInRectSoapOut">
    <wsdl:part name="parameters" element="tns:GetPlaceListInRectResponse" />
  </wsdl:message>
  <wsdl:message name="GetThemeSoapIn">
    <wsdl:part name="parameters" element="tns:GetTheme" />
  </wsdl:message>
  <wsdl:message name="GetThemeSoapOut">
    <wsdl:part name="parameters" element="tns:GetThemeResponse" />
  </wsdl:message>
  <wsdl:message name="GetTileMetaFromLonLatPtSoapIn">
    <wsdl:part name="parameters" element="tns:GetTileMetaFromLonLatPt" />
  </wsdl:message>
  <wsdl:message name="GetTileMetaFromLonLatPtSoapOut">
    <wsdl:part name="parameters" element="tns:GetTileMetaFromLonLatPtResponse" />
  </wsdl:message>
  <wsdl:message name="GetTileMetaFromTileIdSoapIn">
    <wsdl:part name="parameters" element="tns:GetTileMetaFromTileId" />
  </wsdl:message>
  <wsdl:message name="GetTileMetaFromTileIdSoapOut">
    <wsdl:part name="parameters" element="tns:GetTileMetaFromTileIdResponse" />
  </wsdl:message>
  <wsdl:message name="GetTileSoapIn">
    <wsdl:part name="parameters" element="tns:GetTile" />
  </wsdl:message>
  <wsdl:message name="GetTileSoapOut">
    <wsdl:part name="parameters" element="tns:GetTileResponse" />
  </wsdl:message>
  <wsdl:portType name="TerraServiceSoap">
    <wsdl:operation name="ConvertLonLatPtToNearestPlace">
      <wsdl:input message="tns:ConvertLonLatPtToNearestPlaceSoapIn" />
      <wsdl:output message="tns:ConvertLonLatPtToNearestPlaceSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="ConvertLonLatPtToUtmPt">
      <wsdl:input message="tns:ConvertLonLatPtToUtmPtSoapIn" />
      <wsdl:output message="tns:ConvertLonLatPtToUtmPtSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="ConvertUtmPtToLonLatPt">
      <wsdl:input message="tns:ConvertUtmPtToLonLatPtSoapIn" />
      <wsdl:output message="tns:ConvertUtmPtToLonLatPtSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="ConvertPlaceToLonLatPt">
      <wsdl:input message="tns:ConvertPlaceToLonLatPtSoapIn" />
      <wsdl:output message="tns:ConvertPlaceToLonLatPtSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="CountPlacesInRect">
      <wsdl:input message="tns:CountPlacesInRectSoapIn" />
      <wsdl:output message="tns:CountPlacesInRectSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromPt">
      <wsdl:input message="tns:GetAreaFromPtSoapIn" />
      <wsdl:output message="tns:GetAreaFromPtSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromRect">
      <wsdl:input message="tns:GetAreaFromRectSoapIn" />
      <wsdl:output message="tns:GetAreaFromRectSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromTileId">
      <wsdl:input message="tns:GetAreaFromTileIdSoapIn" />
      <wsdl:output message="tns:GetAreaFromTileIdSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetLatLonMetrics">
      <wsdl:input message="tns:GetLatLonMetricsSoapIn" />
      <wsdl:output message="tns:GetLatLonMetricsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetPlaceFacts">
      <wsdl:input message="tns:GetPlaceFactsSoapIn" />
      <wsdl:output message="tns:GetPlaceFactsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetPlaceList">
      <wsdl:input message="tns:GetPlaceListSoapIn" />
      <wsdl:output message="tns:GetPlaceListSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetPlaceListInRect">
      <wsdl:input message="tns:GetPlaceListInRectSoapIn" />
      <wsdl:output message="tns:GetPlaceListInRectSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetTheme">
      <wsdl:input message="tns:GetThemeSoapIn" />
      <wsdl:output message="tns:GetThemeSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetTileMetaFromLonLatPt">
      <wsdl:input message="tns:GetTileMetaFromLonLatPtSoapIn" />
      <wsdl:output message="tns:GetTileMetaFromLonLatPtSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetTileMetaFromTileId">
      <wsdl:input message="tns:GetTileMetaFromTileIdSoapIn" />
      <wsdl:output message="tns:GetTileMetaFromTileIdSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="GetTile">
      <wsdl:input message="tns:GetTileSoapIn" />
      <wsdl:output message="tns:GetTileSoapOut" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="TerraServiceSoap" type="tns:TerraServiceSoap">
    <soap:binding transport="https://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="ConvertLonLatPtToNearestPlace">
      <soap:operation soapAction="https://terraservice-usa.com/ConvertLonLatPtToNearestPlace" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ConvertLonLatPtToUtmPt">
      <soap:operation soapAction="https://terraservice-usa.com/ConvertLonLatPtToUtmPt" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ConvertUtmPtToLonLatPt">
      <soap:operation soapAction="https://terraservice-usa.com/ConvertUtmPtToLonLatPt" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ConvertPlaceToLonLatPt">
      <soap:operation soapAction="https://terraservice-usa.com/ConvertPlaceToLonLatPt" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CountPlacesInRect">
      <soap:operation soapAction="https://terraservice-usa.com/CountPlacesInRect" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromPt">
      <soap:operation soapAction="https://terraservice-usa.com/GetAreaFromPt" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromRect">
      <soap:operation soapAction="https://terraservice-usa.com/GetAreaFromRect" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetAreaFromTileId">
      <soap:operation soapAction="https://terraservice-usa.com/GetAreaFromTileId" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetLatLonMetrics">
      <soap:operation soapAction="https://terraservice-usa.com/GetLatLonMetrics" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetPlaceFacts">
      <soap:operation soapAction="https://terraservice-usa.com/GetPlaceFacts" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetPlaceList">
      <soap:operation soapAction="https://terraservice-usa.com/GetPlaceList" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetPlaceListInRect">
      <soap:operation soapAction="https://terraservice-usa.com/GetPlaceListInRect" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetTheme">
      <soap:operation soapAction="https://terraservice-usa.com/GetTheme" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetTileMetaFromLonLatPt">
      <soap:operation soapAction="https://terraservice-usa.com/GetTileMetaFromLonLatPt" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetTileMetaFromTileId">
      <soap:operation soapAction="https://terraservice-usa.com/GetTileMetaFromTileId" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetTile">
      <soap:operation soapAction="https://terraservice-usa.com/GetTile" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="TerraService">
    <documentation xmlns="https://schemas.xmlsoap.org/wsdl/">TerraServer Web Service</documentation>
    <wsdl:port name="TerraServiceSoap" binding="tns:TerraServiceSoap">
      <soap:address location="https://terraservice.net/TerraService2.asmx" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

## Related topics

<dl> <dt>

[**WS\_HTTP\_PROXY\_SETTING\_MODE\_CUSTOM**](/windows/desktop/api/WebServices/ne-webservices-ws_http_proxy_setting_mode)
</dt> </dl>

 

 




