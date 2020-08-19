---
title: Creating a Service Provider
description: Creating a Service Provider
ms.assetid: 7da27fe2-8a57-4adb-94b2-448b6362dc33
keywords:
- Windows Media Device Manager,creating service providers
- Device Manager,creating service providers
- Windows Media Device Manager,programming guide
- Device Manager,programming guide
- programming guide,service providers
- programming guide,Windows Media Device Manager
- programming guide,creating service providers
- Windows Media Device Manager,service providers
- Device Manager,service providers
- service providers,creating
- creating service providers,about
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Service Provider

A service provider is component that serves as a middleman between an application and a device. Windows Media Device Manager routes requests from the application to the service provider, which is then responsible for communicating with the device or performing the requested action. A service provider usually communicates with a driver to enable communication with the device. A service provider is a COM component that implements the interfaces called by Windows Media Device Manager. The root interface of the service provider object is [**IMDServiceProvider**](/windows/desktop/api/mswmdm/nn-mswmdm-imdserviceprovider). After obtaining this interface, Windows Media Device Manager can obtain other interfaces through the service provider's implementation of various methods. The interfaces that a service provider must implement are listed in [Mandatory and Optional Interfaces](mandatory-and-optional-interfaces.md). The hierarchy of interfaces is shown in [Interfaces for Service Providers](interfaces-for-service-providers.md).

> [!Note]  
> You should not try to create an MTP service provider; instead, you should use the MTP service provider and drivers provided by Microsoft.

 

Before trying to create a service provider, you should thoroughly understand what calls an application will make on a service provider. Read [Creating a Windows Media Device Manager Application](creating-a-windows-media-device-manager-application.md) to get some idea of the basic tasks and calls that an application will make on a service provider when it is attempting to communicate with a device.

The following list shows the key steps in developing a service provider:

1.  Include (and optionally compile) the required header and library files for your project. See [Required Libraries and Headers for a Service Provider](required-libraries-and-headers-for-a-service-provider.md) for the list of required files.
2.  Implement all the other required or optional service provider interfaces (see [Mandatory and Optional Interfaces](mandatory-and-optional-interfaces.md)). Typically, interfaces will be called in this order:
    -   [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate)
    -   [**IMDServiceProvider**](/windows/desktop/api/mswmdm/nn-mswmdm-imdserviceprovider)/2
    -   [**IMDSPEnumDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspenumdevice)
    -   [**IMDSPDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspdevice)/2
    -   [**IMDSPEnumStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspenumstorage)
    -   [**IMDSPStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspstorage)/2/3
3.  Be sure your service provider or device installs the proper registry keys during installation. These keys specify device parameters, register the service provider as a plug-in, and enable Plug and Play notifications for device arrival and removal. See [Device Parameters](device-parameters.md), [Registering the Service Provider](registering-the-service-provider.md), and [Enabling PnP for Devices](enabling-pnp-for-devices.md).
4.  On instantiation of your class, authenticate the service provider in the constructor. To do this, create a [CSecureChannelServer](csecurechannelserver-class.md) class and set the certificate. Implement the [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface and call the methods of the CSecureChannelServer class instantiated previously. See [Authenticating the Service Provider](authenticating-the-service-provider.md) to learn how to instantiate the CSecureChannelServer class and implement the IComponentAuthenticate methods.
5.  Windows Media Device Manager will query your service provider for a list of connected devices by calling [**IMDServiceProvider2::CreateDevice**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider2-createdevice) or [**IMDServiceProvider::EnumDevices**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider-enumdevices), depending on whether the service provider handles Plug and Play devices. The service provider must return a list of [**IMDSPDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-imdspdevice) objects representing connected devices. See [Enumerating Devices](enumerating-devices-service-provider.md) for more details.
6.  Before handling any call, verify that a secure channel has been established. Call [**CSecureChannelServer::fIsAuthenticated**](/previous-versions/bb231600(v=vs.85)) before performing any actions. If this call fails, return WMDM\_E\_NOTCERTIFIED.
7.  You will need a certificate/key pair issued by Microsoft to be able to handle DRM-protected material. See [Handling Protected Content in the Service Provider](handling-protected-content-in-the-service-provider.md) for more information.
8.  To enable your device to synchronize automatically with Windows Media Player, it must fulfill the requirements listed in [Enabling Synchronization with Windows Media Player](enabling-synchronization-with-windows-media-player.md).
9.  To enable your device to appear in Windows Explorer, you must take a few special steps, detailed in [Requirements for Portable Audio Players to Appear in Windows Explorer](requirements-for-portable-audio-players-to-appear-in-windows-explorer.md).

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 