---
title: Using Custom Annotations
description: This topic describes ???
keywords:
ms.topic: article
ms.date: 12/13/2022
---

# Using Custom Annotations

UIAutomation (UIA) Custom Annotations can be used in scenarios where text range attributes do not provide sufficient information for complex applications that require richer annotations (such as Word and Excel).

## Overview

UIAutomation (UIA) uses both elements and text ranges to represent application UI to a client: Elements have [properties](uiauto-propertiesoverview.md) and text ranges have [attributes](uiauto-textattributes.md).

One type of text range attribute is an [**Annotation**](uiauto-textattributes.md#annotation-attributes), essentially metadata containing extra information about content such as a comment in the margin of a document that is associated with text or spreadsheet cell. An annotation is made up of both a known type ID, such as [AnnotationType_Comment]((uiauto-annotation-type-identifiers.md)), and a UI automation element containing properties associated with the annotation, such as the author, date, and so on. The annotation specific information can be retrieved through the [get_CurrentAnnotationTypes method](/windows/win32/api/uiautomationclient/nf-uiautomationclient-iuiautomationelement4-get_currentannotationtypes) or the [get_CachedAnnotationTypes method](/windows/win32/api/uiautomationclient/nf-uiautomationclient-iuiautomationelement4-get_cachedannotationtypes).

Where UIA text range attributes do not provide sufficient information, custom annotations can be used.

> [!NOTE]
> [AnnotationType_Unknown](uiauto-annotation-type-identifiers.md) can be specified on an annotation object to provide an annotation type name through the [annotation pattern](uiauto-implementingannotation.md). However, this annotation type name is localized cannot be used by Accessible Technologies (ATs) that need to get a specific custom annotation.

### Providers

To use custom annotations, a UIA provider must register the custom annotation types that it can return by calling [RegisterAnnotationType](/uwp/api/windows.ui.uiautomation.core.coreautomationregistrar.registerannotationtype). The annotation types can be batch registered on startup, or each can be lazily registered before being returned. When registering an annotation type, the provider supplies a GUID, and UIA returns an integer ID for that annotation, valid within that process.

When returning an annotation type or array of annotation types as the value of a property or text attribute, the provider returns the integer ID it received from UIA, just as it would return the pre-defined integer ID for any standard annotation type. For examples of custom annotations provided by Word, see [Word Custom Annotations](/office/uia/word/wordcustomannotations).

### Clients

A UIA client uses the same [RegisterAnnotationType](/uwp/api/windows.ui.uiautomation.core.coreautomationregistrar.registerannotationtype) method to register all the custom annotation types that it knows about. For each annotation type it must use the same GUID as the provider. It must do this before requesting a property or text attribute where the value is an annotation type (or array of annotation types).

As with the provider side, when the client registers a custom annotation type, UIA returns a corresponding integer ID that is valid within that process. Then, when a provider returns a custom annotation type in the value of a property or text attribute (and the client has registered that same annotation type), UIA will return the same integer ID that it returned during registration. The client can then look for that ID just as it would look for the pre-defined integer ID of a standard annotation type. Custom annotations can be treated like traditional annotations and their usage is identical to normal annotations.

## Example

The following UIA client example shows how to register a [Word Custom Annotation](/office/uia/word/wordcustomannotations) to use with with other UIA APIs. Registration typically occurs when the AT app starts, while the registered GUIDs are unregistered when the AT app shuts down. The [RegisterAnnotationType](/uwp/api/windows.ui.uiautomation.core.coreautomationregistrar.registerannotationtype) method returns a WinRT [AutomationAnnotationTypeRegistration Struct](/uwp/api/windows.ui.uiautomation.core.automationannotationtyperegistration).

```cpp
template <class TElement>

class SafeArrayAccessor
{
public:
    SafeArrayAccessor() = default;
    SafeArrayAccessor(_In_ SAFEARRAY* safeArray, VARTYPE vtExpected)
    {
        THROW_IF_FAILED(Access(safeArray, vtExpected));
    }

    ~SafeArrayAccessor()
    {
        if (m_safeArray != nullptr)
        {
            ::SafeArrayUnaccessData(m_safeArray);
        }
    }

    SafeArrayAccessor(const SafeArrayAccessor& rhs) = delete;
    SafeArrayAccessor& operator=(const SafeArrayAccessor& rhs) = delete;
    SafeArrayAccessor(SafeArrayAccessor&& rhs) = delete;
    SafeArrayAccessor& operator=(SafeArrayAccessor&& rhs) = delete;
    HRESULT Access(_In_ SAFEARRAY* safeArray, VARTYPE vtExpected) noexcept
    {
        RETURN_HR_IF(E_UNEXPECTED, m_safeArray != nullptr);
        RETURN_HR_IF_NULL(E_INVALIDARG, safeArray);
        m_safeArray = safeArray;

        // Check that it's a 1-D array of the expected type.
        RETURN_HR_IF(E_INVALIDARG, ::SafeArrayGetDim(m_safeArray) != 1);
        VARTYPE actualType;
        RETURN_IF_FAILED(::SafeArrayGetVartype(m_safeArray, &actualType));
        if (actualType != vtExpected)
        {
            // Special case to deal with SafeArrays from managed code
            // Managed interop will bring in arrays of ints as VT_INT
            // This is functionally the same as VT_I4 for this code, so
            // allow them to pass as VT_I4.
            // Actually converting them to VT_I4 arrays would mean full
            // array copies, which would both make the code more complex
            // and less perfomant, making this short-circuit the best way
            // to allow them through.
            RETURN_HR_IF(E_INVALIDARG, 
               !(actualType == VT_INT && vtExpected == VT_I4));
        }
        LONG lb;
        LONG ub;
        RETURN_IF_FAILED(::SafeArrayGetLBound(m_safeArray, 1, &lb));
        RETURN_IF_FAILED(::SafeArrayGetUBound(m_safeArray, 1, &ub));
        m_count = ub - lb + 1;
        RETURN_IF_FAILED(::SafeArrayAccessData(m_safeArray, 
           reinterpret_cast<void**>(&m_data)));
        return S_OK;
    }

    UINT Count() const noexcept
    {
        return m_count;
    }

    const TElement& operator[](UINT i) const noexcept
    {
        return m_data[i];
    }

    TElement& operator[](UINT i) noexcept
    {
        return m_data[i];
    }

    operator TElement*() noexcept
    {
        return m_data;
    }

    TElement* Ptr() noexcept
    {
        return m_data;
    }

private:
    SAFEARRAY* m_safeArray = nullptr;
    UINT m_count = 0;
    TElement* m_data = nullptr;
};

enum class CustomWordAnnotation
{
    BookMark = 0,
    DraftComment,
    ResolvedComment,
    None,
};

using unique_safearray = 
   wil::unique_any<SAFEARRAY*, 
   decltype(&::SafeArrayDestroy), 
   ::SafeArrayDestroy>;

class CustomAnnotationUtility
{
public:
    CustomAnnotationUtility()
    {
       static constexpr winrt::guid c_Bookmark{ 
          GUID{ 0x25330951, 0xA372, 0x4DB9, { 0x48, 0x8A, 0x85, 0x13, 0x7A, 0xD0, 0x08, 0xD2 } } };
       m_bookmarkRegId = winrt::CoreAutomationRegistrar::RegisterAnnotationType(c_Bookmark);
       m_bookMark = m_bookmarkRegId.LocalId;
       static constexpr winrt::guid c_DraftComment{ 
          GUID{ 0x26BAEBC6, 0x591E, 0x4116, { 0xBB, 0xCF, 0xE9, 0xA7, 0x99, 0x6C, 0xD1, 0x69 } } };
       m_draftCommentRegId = 
          winrt::CoreAutomationRegistrar::RegisterAnnotationType(c_DraftComment);
       m_draftComment = m_draftCommentRegId. LocalId;
       static constexpr winrt::guid c_ResolvedComment{ 
          GUID{ 0xA015030C, 0x5B44, 0x4EAC, { 0xB0, 0xCC, 0x21, 0xBA, 0x35, 0xDE, 0x6D, 0x07 } } };
       m_resolvedCommentRegId = 
          winrt::CoreAutomationRegistrar::RegisterAnnotationType(c_ResolvedComment);
       m_resolvedComment = m_resolvedCommentRegId.LocalId;
    }

    ~CustomAnnotationUtility()
    {
        winrt::CoreAutomationRegistrar::UnregisterAnnotationType(
           m_bookmarkRegId);
        winrt::CoreAutomationRegistrar::UnregisterAnnotationType(
           m_draftCommentRegId);
        winrt::CoreAutomationRegistrar::UnregisterAnnotationType(
           m_resolvedCommentRegId);
    }

    // Get custom annotations from text pattern of the automation element.
    std::vector<CustomWordAnnotation> GetCustomWordAnnotationsFrom(
       _In_ IUIAutomationTextPattern* textPattern)
    {
        wil::com_ptr<IUIAutomationTextRange> textRange;
        VERIFY_SUCCEEDED(textPattern->get_DocumentRange(&textRange));
        wil::unique_variant annotationTypesVariant;
        VERIFY_SUCCEEDED(textRange->GetAttributeValue(
           UIA_AnnotationTypesAttributeId, &annotationTypesVariant));
        VERIFY_ARE_EQUAL(VT_I4 | VT_ARRAY, annotationTypesVariant.vt);
        SafeArrayAccessor<int> annotationTypes(
           annotationTypesVariant.parray, VT_I4);
        std::vector<CustomWordAnnotation> customAnnotations;
        for (unsigned int i = 0; i < annotationTypes.Count(); i++)
        {
            int annotation = annotationTypes[i];
            if (annotation == m_bookMark)
            {
                customAnnotations.emplace_back(
                   CustomWordAnnotation::BookMark);
            }
            else if (annotation == m_draftComment)
            {
                customAnnotations.emplace_back(
                   CustomWordAnnotation::DraftComment);
            }
            else if (annotation == m_resolvedComment)
            {
                customAnnotations.emplace_back(
                   CustomWordAnnotation::ResolvedComment);
            }
        }
        return customAnnotations;
    }

    // Driver Function
    std::vector<CustomWordAnnotation> 
       ExtractAllCustomAnnotationFromTextPatternOf(
          _In_ IUIAutomationElement* wordElement)
    {
        wil::com_ptr<IUIAutomationTextPattern> textPattern;
        VERIFY_SUCCEEDED(wordElement->GetCurrentPatternAs(
           UIA_TextPatternId, IID_PPV_ARGS(&textPattern)));
        VERIFY_IS_NOT_NULL(textPattern);
        return GetCustomWordAnnotationsFrom (textPattern.get());
    }

    // Get custom annotations from given automation element.
    std::vector<CustomWordAnnotation> GetCustomWordAnnotationsFromElement(
       _In_ IUIAutomationElement* wordElement)
    {
        wil::com_ptr<IUIAutomationElement4> wordElement4 = 
           wil::com_query<IUIAutomationElement4>(wordElement);
        unique_safearray annotationTypesSafeArray;
        VERIFY_SUCCEEDED(wordElement4->get_CurrentAnnotationTypes(
           &annotationTypesSafeArray));
        VERIFY_ARE_EQUAL(VT_I4 | VT_ARRAY, annotationTypesVariant.vt);
        SafeArrayAccessor<int> annotationTypes(
           annotationTypesSafeArray.get(), VT_I4);
        std::vector<CustomWordAnnotation> customAnnotations;
        for (unsigned int i = 0; i < annotationTypes.Count(); i++)
        {
            Int annotation = annotationTypes[i];
            if (annotation == m_bookMark)
            {
                customAnnotations.emplace_back(
                   CustomWordAnnotation::BookMark);
            }
            else if (annotation == m_draftComment)
            {
                customAnnotations.emplace_back(CustomWordAnnotation::DraftComment);
            }
            else if (annotation == m_resolvedComment)
            {
                customAnnotations.emplace_back(CustomWordAnnotation::ResolvedComment);
            }
        }
        return customAnnotations;
    }

    std::vector<CustomWordAnnotation> 
       GetCustomAnnotationUsingCachedAnnotationTypesProperty(
         _In_ IUIAutomationElement* wordElement)
    {
        wil::com_ptr<IUIAutomation> automation = 
           wil::CoCreateInstance<CUIAutomation8, IUIAutomation>();
        wil::com_ptr<IUIAutomationCacheRequest> cacheRequest;
        VERIFY_SUCCEEDED(automation->CreateCacheRequest(&cacheRequest));
        VERIFY_SUCCEEDED(cacheRequest->AddProperty(UIA_AnnotationTypesPropertyId));
        wil::com_ptr<IUIAutomationElement> cachedWordElement;
        VERIFY_SUCCEEDED(wordElement->BuildUpdatedCache(cacheRequest.get(), &cachedWordElement));
        wil::com_ptr<IUIAutomationElement4> cachedWordElement4 = 
           wil::com_query<IUIAutomationElement4>(cachedWordElement);
        unique_safearray annotationTypesSafeArray;
        VERIFY_SUCCEEDED(cachedWordElement4->get_CachedAnnotationTypes(&annotationTypesSafeArray));
        SafeArrayAccessor<int> annotationTypes(annotationTypesSafeArray.get(), VT_I4);
        std::vector<CustomWordAnnotation> customAnnotations;
        for (unsigned int i = 0; i < annotationTypes.Count(); i++)
        {
            int annotation = annotationTypes[i];
            if (annotation == m_bookMark)
            {
                customAnnotations.emplace_back(CustomWordAnnotation::BookMark);
            }
            else if (annotation == m_draftComment)
            {
                customAnnotations.emplace_back(CustomWordAnnotation::DraftComment);
            }
            else if (annotation == m_resolvedComment)
            {
                customAnnotations.emplace_back(CustomWordAnnotation::ResolvedComment);
            }
        }
        return customAnnotations;
    }

    CustomWordAnnotation 
       GetAnnotationFromAnnotationPattern(_In_ IUIAutomationElement* wordElement)
    {
        wil::com_ptr<IUIAutomationAnnotationPattern> annotationPattern;
        VERIFY_SUCCEEDED(wordElement->GetCurrentPatternAs(
           UIA_AnnotationPatternId, IID_PPV_ARGS(&annotationPattern)));
        VERIFY_IS_NOT_NULL(annotationPattern);
        int annotation;
        VERIFY_SUCCEEDED(annotationPattern->get_CurrentAnnotationTypeId(&annotation));
        if (annotation == m_bookMark)
        {
            return CustomWordAnnotation::BookMark;
        }
        else if (annotation == m_draftComment)
        {
            return CustomWordAnnotation::DraftComment;
        }
        else if (annotation == m_resolvedComment)
        {
            return CustomWordAnnotation::ResolvedComment;
        }
        return CustomWordAnnotation::None;
    }

    // Finds an element in tree that has the bookmark custom annotation.
    wil::com_ptr<IUIAutomationElement> 
       FindElementWithBookmarkCustomAnnotation(_In_ IUIAutomationElement* startElement)
    {
        wil::com_ptr<IUIAutomation> automation = 
           wil::CoCreateInstance<CUIAutomation8, IUIAutomation>();
        wil::unique_variant annotationTypeVariant;
        annotationTypeVariant.vt = VT_I4;
        annotationTypeVariant.lVal = m_bookMark;
        wil::com_ptr<IUIAutomationCondition> annotationTypeCondition;
        VERIFY_SUCCEEDED(automation->CreatePropertyCondition(
           UIA_AnnotationAnnotationTypeIdPropertyId, annotationTypeVariant, &annotationTypeCondition));
        wil::com_ptr<IUIAutomationCacheRequest> cacheRequest;
        VERIFY_SUCCEEDED(automation->CreateCacheRequest(&cacheRequest));
        VERIFY_SUCCEEDED(cacheRequest->AddPattern(UIA_AnnotationPatternId));
        VERIFY_SUCCEEDED(cacheRequest->AddProperty(UIA_AnnotationAnnotationTypeIdPropertyId));
        wil::com_ptr<IUIAutomationElement> annotationObject;
        VERIFY_SUCCEEDED(startElement->FindFirstBuildCache(
           TreeScope_Descendants, annotationTypeCondition.get(), cacheRequest.get(), &annotationObject));
        return annotationObject;
    }

    // Finds a custom annotation element using the item container property.
    wil::com_ptr<IUIAutomationElement> 
       FindDraftCommentCustomAnnotationElementUsingItemContainerProperty(
          _In_ IUIAutomationElement* wordElement)
    {
        wil::com_ptr<IUIAutomationItemContainerPattern> itemContainerPattern;
        VERIFY_SUCCEEDED(wordElement->GetCurrentPatternAs(
           UIA_ItemContainerPatternId, IID_PPV_ARGS(&itemContainerPattern)));
        VERIFY_IS_NOT_NULL(itemContainerPattern);
        wil::unique_variant annotationTypeVariant;
        annotationTypeVariant.vt = VT_I4;
        annotationTypeVariant.lVal = m_draftComment;
        wil::com_ptr<IUIAutomationElement> annotationObject;
        VERIFY_SUCCEEDED(itemContainerPattern->FindItemByProperty(
            nullptr /* startAfter */,
            UIA_AnnotationAnnotationTypeIdPropertyId,
            annotationTypeVariant,
            &annotationObject));
        return annotationObject;
    }

    // Extracts a text range that has a given custom annotation.
    wil::com_ptr<IUIAutomationTextRange> 
       FindTextRangeWithResolvedCommentCustomAnnotation(
          _In_ IUIAutomationTextRange* wordDocRange)
    {
        wil::unique_variant targetVariant;
        targetVariant.vt = VT_I4;
        targetVariant.lVal = m_resolvedComment;
        wil::com_ptr<IUIAutomationTextRange> resultRange;
        VERIFY_SUCCEEDED(wordDocRange ->FindAttribute(
           UIA_AnnotationTypesAttributeId, 
           targetVariant, FALSE /* backward */, &resultRange));
        return resultRange;
    }

private:
    int m_bookMark;
    int m_draftComment;
    int m_resolvedComment;
    winrt:: AutomationAnnotationTypeRegistration m_bookmarkRegId;
    winrt:: AutomationAnnotationTypeRegistration m_draftCommentRegId;
    winrt:: AutomationAnnotationTypeRegistration m_resolvedCommentRegId;
};

void main()
{
    // AT (such as Narrator, NVDA, JAWS) is focused on Word document of 
    // version that supports the custom annotations.
    // Assumption: All properties and patterns used below are 
    // assumed to be supported by the focused element.
    wil::com_ptr<IUIAutomation> automation = 
       wil::CoCreateInstance<CUIAutomation8, IUIAutomation>();
    VERIFY_IS_NOT_NULL(automation);
    wil::com_ptr<IUIAutomationElement> focusedElement;
    VERIFY_SUCCEEDED(automation->GetFocusedElement(&focusedElement));
    CustomAnnotationUtility customAnnotationUtility;
    std::vector<CustomWordAnnotation> textPatternAnnotations = 
       customAnnotationUtility.ExtractAllCustomAnnotationFromTextPatternOf(
          focusedElement.get());
    std::vector<CustomWordAnnotation> elementAnnotations = 
       customAnnotationUtility. GetCustomWordAnnotationsFromElement (
          focusedElement.get());
    std::vector<CustomWordAnnotation> cachedElementAnnotations = 
       customAnnotationUtility.GetCustomAnnotationUsingCachedAnnotationTypesProperty(
          focusedElement.get());
    CustomWordAnnotation annotationPatternAnnotations = 
       customAnnotationUtility.GetAnnotationFromAnnotationPattern(
          focusedElement.get());
    wil::com_ptr<IUIAutomationElement> bookMarkElement = 
       customAnnotationUtility. FindElementWithBookmarkCustomAnnotation(
          focusedElement.get());
    wil::com_ptr<IUIAutomationElement> draftCommentElement = 
       customAnnotationUtility. FindDraftCommentCustomAnnotationElementUsingItemContainerProperty(
          focusedElement.get());
    wil::com_ptr<IUIAutomationTextPattern> textPattern;
    VERIFY_SUCCEEDED(focusedElement->GetCurrentPatternAs(
       UIA_TextPatternId, IID_PPV_ARGS(&textPattern)));
    VERIFY_IS_NOT_NULL(textPattern);
    wil::com_ptr<IUIAutomationTextRange> documentRange;
    VERIFY_SUCCEEDED(textPattern->get_DocumentRange(&documentRange));
    wil::com_ptr<IUIAutomationTextRange> resolvedCommentRange = 
       customAnnotationUtility.FindTextRangeWithResolvedCommentCustomAnnotation(
          documentRange.get());
}
```

## See also

- [RegisterAnnotationType Method](/uwp/api/windows.ui.uiautomation.core.coreautomationregistrar.registerannotationtype)
- [AutomationAnnotationTypeRegistration Struct](/uwp/api/windows.ui.uiautomation.core.automationannotationtyperegistration)
- [Word Custom Annotations](/office/uia/word/wordcustomannotations)
- [Annotation Control Pattern](uiauto-implementingannotation.md)
- [Annotation Type Identifiers](uiauto-annotation-type-identifiers.md)
