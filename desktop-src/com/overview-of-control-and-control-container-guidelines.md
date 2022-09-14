---
title: Overview of Control and Control Container Guidelines
description: Overview of Control and Control Container Guidelines
ms.assetid: c4cf2409-0085-43e6-afa2-f9c03cc50565
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Control and Control Container Guidelines

An ActiveX control is essentially a simple OLE object that supports the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. It will usually support more interfaces in order to offer functionality, but all additional interfaces may be viewed as optional and as such, a control container should not rely on any additional interfaces being supported. By not specifying additional interfaces that a control must support, a control may efficiently target a particular area of functionality without having to support particular interfaces to qualify as a control. As always with OLE, whether in a control or a control container, it should never be assumed that an interface is available and standard return-checking conventions should always be followed. It is important for a control or control container to degrade gracefully and offer alternative functionality if an interface required is not available.

An ActiveX control container must be able to host a minimal ActiveX control; it will also support a number of additional interfaces as specified in [Containers](containers.md). There are a number of interfaces and methods that a container may optionally support, which are grouped into functional areas known as *component categories*. A container may support any combination of component categories, for example, a component category exists for databinding and a container may or may not support the databinding functionality, depending on the market needs of the container. If a control needs databinding support from a container to function, then it will enter this requirement in the registry. This allows a control container to only offer for insertion those controls that it knows it can successfully host. It is important to note that component categories are specified as part of OLE and are not specific to ActiveX controls, the controls architecture uses component categories to identify areas of functionality that an OLE component may support. Component categories are not cumulative or exclusive, so a control container can support one category without necessarily supporting another.

It is important for controls that require optional features, or features specific to a certain container to be clearly packaged and marketed with those requirements. Similarly containers that offer certain features or component categories must be marketed and packaged as offering those levels of support when hosting ActiveX controls. It is recommended that controls target and test with as many containers as possible and degrade gracefully to offer less or alternative functionality if interfaces or methods are not available. In a situation where a control cannot perform its designated job function without the support of a component category, that category should be entered as a requirement in the registry in order to prevent the control being inserted in an inappropriate container.

These guidelines define those interfaces and methods that a control may expect a control container to support, although as always a control should check the return values when using [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) or other methods to obtain pointers to these interfaces. A container should not expect a control to support anything more than the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface, and these guidelines identify what interfaces a control may support and what the presence of a particular interface means.

## Why the ActiveX Control and Control Container Guidelines Are Important

ActiveX Controls have become the primary architecture for developing programmable software components for use in a variety of different containers ranging from software development tools to end-user productivity tools. In order for a control to operate well in a variety of containers, the control must be able to assume some minimum level of functionality that it can rely on in all containers.

By following these guidelines, control and container developers make their controls and containers more reliable and interoperable, and ultimately, better and more usable components for building component-based solutions.

## What to Do When an Interface You Need Is Not Available

OLE programs should use [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) to acquire interface pointers, and must check the return value. OLE applications cannot safely assume that **QueryInterface** will succeed.

This requirement applies to all OLE applications. If the requested interface is not available (that is, [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) returns E\_NOINTERFACE), the control or container must degrade gracefully, even if that means that it cannot perform its designated job function.

## Related topics

<dl> <dt>

[ActiveX Control and Control Container Guidelines](activex-control-and-control-container-guidelines.md)
</dt> </dl>

 

 




