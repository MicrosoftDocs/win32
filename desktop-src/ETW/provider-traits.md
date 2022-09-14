---
description: Provider Traits are a method of attaching more data to an individual provider registration.
ms.assetid: 97755D64-BF57-4C0D-8ED4-040FC375C4AF
title: Provider Traits
ms.topic: article
ms.date: 05/31/2018
---

# Provider Traits

Provider Traits are a method of attaching more data to an individual provider registration. They can be used for manifest-based or TraceLogging providers. This currently includes support for adding a Provider Name and/or Provider Group to an individual provider registration. More trait types are likely to be added in the future. This information is stored in the kernel as a binary blob of a set format.

Traits can only be set once for a registration. Any further attempts to set the traits on that registration will fail.

To set Provider Traits on a manifest-based provider, call the [**EventSetInformation**](/windows/desktop/api/Evntprov/nf-evntprov-eventsetinformation) function with the EventProviderSetTraits information class. The EventInformation buffer should contain a binary blob of the following format:

``` syntax
{
   UINT16 TraitsSize   // Total size of the traits including this field
   CHAR[] ProviderName // Null terminated utf-8 provider name
   TRAIT[] Traits      // Zero or more individual traits
}
```

Individual traits should be in the following format:

``` syntax
TRAIT {
      UINT16 TraitSize // Size of this individual trait including this field
      UINT8 Type       // ETW_PROVIDER_TRAIT_TYPE
      BYTE[] Data
      }
```

From the individual trait, ETW\_PROVIDER\_TRAIT\_TYPE is defined as:

``` syntax
typedef enum {
    EtwProviderTraitTypeGroup = 1,
    EtwProviderTraitTypeMax
} ETW_PROVIDER_TRAIT_TYPE;
```

TraceLogging providers automatically set the Provider Traits when the [**TraceLoggingRegister**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingregister) function is called. The TraceLogging provider's name will always be included in its traits. A group can be set on a TraceLogging provider using the [**TraceLoggingOptionGroup**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingoptiongroup) macro in the provider definition.

## Custom Traits

Although most of the 255 possible trait types are not yet defined, trait types 1-127 are reserved for definition by Microsoft. The remaining higher indexed type values can be used by external developers as they see fit. Anyone considering adding their own custom traits to their provider should try to keep their total trait size under 256 bytes for the following reasons:

-   The traits are included in every event written for the provider. Large traits could lead to very large log files.
-   The traits are stored in nonpaged kernel pool for the lifetime of the provider.

## Provider Groups

A provider group is a GUID-defined controllable entity much like a provider itself. The key difference is that while a provider GUID is used to control registrations of just its provider, a group will control all of its member registrations. For example, enabling a provider group with a given keyword and level will enable all of the groups member registrations with that keyword and level.

Group membership may be restricted by permissions. If the caller of [**EventSetInformation**](/windows/desktop/api/Evntprov/nf-evntprov-eventsetinformation) doesn't have permissions to join the specified group, then membership will be denied.

In some cases the trace session controller may want to exclude a few providers from its enable of a group. This can be done by setting a disallow list. A disallow list is a list of provider GUIDs that will not be enabled based on the group settings for a single logging session. Disallow lists can be changed dynamically with [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) and the TraceSetDisallowList information class.

While most enable actions can be done for Provider Groups in a similar manner to individual providers, there are some exceptions. Exceptions include:

-   Provider Groups cannot be controlled by private trace sessions.
-   Event Name, Event ID, and Payload filters are not applicable to Provider Groups as they assume specific information of an individual provider.

 

 
