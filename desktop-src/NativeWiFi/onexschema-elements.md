---
title: OneX schema elements
description: An 802.1X profile contains the following schema elements.
ms.topic: article
ms.date: 06/21/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.assetid: be3f1986-d0c2-47f6-b4dd-8defb89bd03a
---

# OneX schema elements

An 802.1X profile contains the following schema elements. All OneX schema elements apply to both wired and wireless profiles. Most of the named elements are in the namespace `https://www.microsoft.com/networking/OneX/v1`, except for [**EAPConfig (OneX)**](onexschema-eapconfig-onex-element.md) which is in the namespace `https://www.microsoft.com/provisioning/EapHostConfig`.

The following list shows the defined elements in the order in which the elements appear in a profile. The ordering of elements is enforced. Not all elements are in every profile, as some elements are optional.

This list does not show all possible elements that can appear in a profile, as elements can be added in **xs:any** insertion points.

## Elements

* [**OneX**](onexschema-onex-element.md)
  * [**cacheUserData (OneX)**](onexschema-cacheuserdata-onex-element.md)
  * [**heldPeriod (OneX)**](onexschema-heldperiod-onex-element.md)
  * [**authPeriod (OneX)**](onexschema-authperiod-onex-element.md)
  * [**startPeriod (OneX)**](onexschema-startperiod-onex-element.md)
  * [**maxStart (OneX)**](onexschema-maxstart-onex-element.md)
  * [**maxAuthFailures (OneX)**](onexschema-maxauthfailures-onex-element.md)
  * [**supplicantMode (OneX)**](onexschema-supplicantmode-onex-element.md)
  * [**authMode (OneX)**](onexschema-authmode-onex-element.md)
  * [**singleSignOn (OneX)**](onexschema-singlesignon-onex-element.md)
    * [**type (singleSignOn)**](onexschema-type-singlesignon-element.md)
    * [**maxDelay (singleSignOn)**](onexschema-maxdelay-singlesignon-element.md)
    * [**userBasedVirtualLan (singleSignOn)**](onexschema-userbasedvirtuallan-singlesignon-element.md)
  * [**EAPConfig (OneX)**](onexschema-eapconfig-onex-element.md)
