---
title: Using Custom Control Patterns
description: This topic describes how UIAutomation (UIA) custom control patterns can be used in scenarios where the predefined UIAutomation patterns do not support the functionality provided by custom UI elements and application scenarios.
keywords:
ms.topic: article
ms.date: 01/11/2023
---

# Using Custom Control Patterns

UIAutomation (UIA) custom control patterns can be used in scenarios where the predefined UIAutomation patterns do not support the functionality provided by custom UI elements and application scenarios.

## Overview

A [UIA control pattern](uiauto-controlpatternsoverview.md) is an interface with properties, methods, and events that define a discrete piece of functionality available to UIA clients.

Control pattern methods allow UI Automation clients to manipulate a particular aspect of the control, while properties and events provide information about some aspect of the control, and provide information about the state of the automation element that implements the control pattern. For example the [Scroll Pattern](/dotnet/api/system.windows.automation.scrollpattern) can be used by a client to perform actions such as [Scroll](/dotnet/api/system.windows.automation.scrollpattern.scroll) and [SetScrollPercent](/dotnet/api/system.windows.automation.scrollpattern.setscrollpercent).

Remote operations form the basis for custom control patterns. Remote operations are UIA client APIs that can be used to batch up a series of calls to an app, reducing a series of cross-process calls to a single transition. For more information on remote operations, see [Windows.UI.UIAutomation.Core Namespace](/uwp/api/windows.ui.uiautomation.core).

> [!NOTE]
> The legacy APIs provide a more limited implementation of custom patterns. We recommend using the latest APIs described in this topic showing how clients use custom patterns in Office apps ([UI Automation Custom Extensions in Office](/office/uia/)).

## Wrapper APIs

The remote operations APIs mentioned above can be difficult to use. For this reason, a set of wrapper APIs ([Microsoft.UI.UIAutomation.idl](https://github.com/microsoft/Microsoft-UI-UIAutomation/blob/main/src/UIAutomation/Microsoft.UI.UIAutomation/Microsoft.UI.UIAutomation.idl) and [UiaOperationAbstraction](https://github.com/microsoft/Microsoft-UI-UIAutomation/tree/main/src/UIAutomation/UiaOperationAbstraction)), intended to simplify constructing and executing remote operations, are available to download from the [Windows UIAutomation platform utility libraries](https://github.com/microsoft/Microsoft-UI-UIAutomation) on GitHub.

The higher-level APIs in [UiaOperationAbstraction](https://github.com/microsoft/Microsoft-UI-UIAutomation/tree/main/src/UIAutomation/UiaOperationAbstraction) and [Microsoft.UI.UIAutomation.idl](https://github.com/microsoft/Microsoft-UI-UIAutomation/blob/main/src/UIAutomation/Microsoft.UI.UIAutomation/Microsoft.UI.UIAutomation.idl) mirror the existing UIA COM APIs. Without these wrapper APIs, the byte codes for different instructions need to be specified manually, which is difficult if remote operations need to execute a large number of opcode instructions. To help UIA clients, we've provided builder APIs that wrap the actual UIA APIs to build byte codes for the client required by the remote operation.

## Examples

### Word example

The following UIA client example shows how to call the new windows APIs specific to custom patterns using the Wrapper APIs. The example uses the [custom UI Automation patterns in Microsoft Word](/office/uia/word/wordcustompatterns).

```cpp
#include <winrt/Microsoft.UI.UIAutomation.h>
#include <winrt/Windows.UI.UIAutomation.h>
#include <winrt/Windows.UI.UIAutomation.Core.h>
namespace winrt
{
    using namespace winrt::Microsoft::UI::UIAutomation;
    using namespace winrt::Windows::UI::UIAutomation;
    using namespace winrt::Windows::UI::UIAutomation::Core;
}

enum class AttributeIdentifier
{
    LineNumber = 0,
    PageNumber,
    ColumnNumber,
    SectionNumber,
    BookmarkName,
};

   template<class T>
    winrt::com_ptr<T> MakeWinrtComPtr(_In_ T* rawPtr)
    {
        winrt::com_ptr<T> ptr;
        ptr.copy_from(rawPtr);
        return ptr;
    }


    class WordCustomPatternDataFetcher
    {
    private:
        winrt::IInspectable m_connectionBoundObject;

    public:

        explicit WordCustomPatternDataFetcher(
			_In_ IUIAutomationElement* enclosingElement)
        {
            m_connectionBoundObject = GetConnectionBoundObject(enclosingElement);
        }

        ~WordCustomPatternDataFetcher() = default;

        winrt::IInspectable GetConnectionBoundObject(
			_In_ IUIAutomationElement* enclosingElement)
        {
            winrt::com_ptr<IUIAutomationElement> winrtElement = 
				MakeWinrtComPtr(enclosingElement);

            // Guid: {93514122-FF04-4B2C-A4AD-4AB04587C129} 
			// to get ITextRangeCustomProvider as a connection bound object.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x93514122, 0xFF04, 0x4B2C, { 
					0xA4, 0xAD, 0x4A, 0xB0, 0x45, 0x87, 0xC1, 0x29 } } };

            // Start a remote operation.
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteElement remoteElement = 
				remoteOperation.ImportElement(winrtElement.as<winrt::AutomationElement>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);

            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteOperation.NewEmpty());
            remoteElement.CallExtension(
				extensionGuid, winrt::array_view(extensionOperands));
            const winrt::AutomationRemoteOperationResponseToken connectionBoundObjectToken = 
				remoteOperation.RequestResponse(extensionOperands[0]);

            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            // Test the pattern object set by the provider.
            const winrt::IInspectable inspectable = 
				results.GetResult(connectionBoundObjectToken);
            return inspectable;
        }

        // Gets attribute value for page, column, section numbers.
        int GetCustomAttributeValue(
			_In_ IUIAutomationTextRange* textRange, 
				AttributeIdentifier attributeIdentifier)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);

            // Guid: {081ACA91-32F2-46F0-9FB9-017038BC45F8} 
			// for word custom annotations on custom pattern objects.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x081ACA91, 0x32F2, 0x46F0, { 
					0x9F, 0xB9, 0x01, 0x70, 0x38, 0xBC, 0x45, 0xF8 } } };

            // Start a remote operation
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the custom method specific to attribute value take 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            // 2. Identifier of custom annotation attribute(line number/page number etc).
            // 3. Output parameter that holds the custom attribute value.
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);
            extensionOperands.emplace_back(
				remoteOperation.NewInt(static_cast<int>(attributeIdentifier)));
            extensionOperands.emplace_back(remoteOperation.NewEmpty());

            remoteConnectionBoundObject.CallExtension(extensionGuid, extensionOperands);

            const winrt::AutomationRemoteOperationResponseToken remoteAttributeToken = 
				remoteOperation.RequestResponse(extensionOperands[2]);
            winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const int attributeValue = 
				winrt::unbox_value<int>(results.GetResult(remoteAttributeToken));
            return attributeValue;
        }

        winrt::hstring GetBookMarkName(_In_ IUIAutomationTextRange* textRange)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);

            // Guid: {081ACA91-32F2-46F0-9FB9-017038BC45F8} 
			// for word custom annotations on custom pattern objects.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x081ACA91, 0x32F2, 0x46F0, { 
					0x9F, 0xB9, 0x01, 0x70, 0x38, 0xBC, 0x45, 0xF8 } } };

            // Start a remote operation
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the custom method specific to attribute value takes 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            // 2. Identifier of custom annotation attribute(line number/page number etc).
            // 3. Output parameter that holds the custom attribute value.
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);
            extensionOperands.emplace_back(
				remoteOperation.NewInt(
					static_cast<int>(AttributeIdentifier::BookmarkName)));
            extensionOperands.emplace_back(remoteOperation.NewEmpty());
            remoteConnectionBoundObject.CallExtension(
				extensionGuid, extensionOperands);

            const winrt::AutomationRemoteOperationResponseToken remoteStringToken = 
				remoteOperation.RequestResponse(extensionOperands[2]);
            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const winrt::hstring attributeValue = 
				winrt::unbox_value<winrt::hstring>(results.GetResult(remoteStringToken));
            return attributeValue;
        }

        std::pair<winrt::AutomationTextRange, int> MoveBySentence(
			_In_ IUIAutomationTextRange* textRange, int moveBy)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);

            // Guid: {F39655AC-133A-435B-A318-C197F0D3D203} 
			// for moving a text range by sentence.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0xF39655AC, 0x133A, 0x435B, { 
					0xA3, 0x18, 0xC1, 0x97, 0xF0, 0xD3, 0xD2, 0x03 } } };

            // Start a remote operation.
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(
					winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the custom method specific to attribute value takes 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            // 2. Number of units to move.
            // 3. Output parameter that gives the number of units moved.
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);
            extensionOperands.emplace_back(remoteOperation.NewInt(moveBy));
            extensionOperands.emplace_back(remoteOperation.NewEmpty());
            remoteConnectionBoundObject.CallExtension(
				extensionGuid, winrt::array_view(extensionOperands));

            const winrt::AutomationRemoteOperationResponseToken remoteModifiedRangeToken = 
				remoteOperation.RequestResponse(extensionOperands[0]);
            const winrt::AutomationRemoteOperationResponseToken remoteMovedByToken = 
				remoteOperation.RequestResponse(extensionOperands[2]);

            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const int movedBy = 
				winrt::unbox_value<int>(results.GetResult(remoteMovedByToken));
            const winrt::IInspectable modifiedInspectableRange = 
				results.GetResult(remoteModifiedRangeToken);
            winrt::AutomationTextRange modifiedRange = 
				modifiedInspectableRange.as<winrt::AutomationTextRange>();
            return { modifiedRange, movedBy };
        }

        std::pair<winrt::AutomationTextRange, int> MoveEndpointBySentence(
			_In_ IUIAutomationTextRange* textRange,
            TextPatternRangeEndpoint endpoint,
            int moveBy)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);

            // Guid: {368E89A2-1BC2-4402-8C58-33C63ECFFA3B} 
			// for moving an endpoint of text range by sentence.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x368E89A2, 0x1BC2, 0x4402, { 
					0x8C, 0x58, 0x33, 0xC6, 0x3E, 0xCF, 0xFA, 0x3B } } };

            // Start a remote operation
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the custom method specific to attribute value takes 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            // 2. Number of units to move.
            // 3. Output parameter that gives the number of units moved.
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);
            extensionOperands.emplace_back(
				remoteOperation.NewInt(static_cast<int>(endpoint)));
            extensionOperands.emplace_back(remoteOperation.NewInt(moveBy));
            extensionOperands.emplace_back(remoteOperation.NewEmpty());

            const winrt::AutomationRemoteOperationResponseToken remoteModifiedRangeToken = 
				remoteOperation.RequestResponse(extensionOperands[0]);
            const winrt::AutomationRemoteOperationResponseToken remoteMovedByToken = 
				remoteOperation.RequestResponse(extensionOperands[3]);

            remoteConnectionBoundObject.CallExtension(
				extensionGuid, extensionOperands);

            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const int movedBy = winrt::unbox_value<int>(
				results.GetResult(remoteMovedByToken));
            const winrt::IInspectable modifiedInspectableRange = 
				results.GetResult(remoteModifiedRangeToken);
            winrt::AutomationTextRange modifiedRange = 
				modifiedInspectableRange.as<winrt::AutomationTextRange>();
            return { modifiedRange, movedBy };
        }

        winrt::AutomationTextRange ExpandToEnclosingSentence(
			_In_ IUIAutomationTextRange* textRange)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);

            // Guid: {98FE8B34-F317-459A-9627-21123EA95BEA} 
			// for expanding to enclosing unit sentence.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x98FE8B34, 0xF317, 0x459A, { 
					0x96, 0x27, 0x21, 0x12, 0x3E, 0xA9, 0x5B, 0xEA } } };

            // Start a remote operation
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(
					winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the custom method specific to attribute value takes 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);

            remoteConnectionBoundObject.CallExtension(
				extensionGuid, extensionOperands);

            const winrt::AutomationRemoteOperationResponseToken remoteModifiedRangeToken = 
				remoteOperation.RequestResponse(extensionOperands[0]);
            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const winrt::IInspectable modifiedInspectableRange = 
				results.GetResult(remoteModifiedRangeToken);
            winrt::AutomationTextRange modifiedRange = 
				modifiedInspectableRange.as<winrt::AutomationTextRange>();
            return modifiedRange;

        }

        winrt::hstring GetMathMarkUp(_In_ IUIAutomationTextRange* textRange)
        {
            winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = 
				MakeWinrtComPtr(textRange);
            // Guid: {98FE8B34-F317-459A-9627-21123EA95BEA} 
			// for expanding to enclosing unit sentence.
            static constexpr winrt::guid extensionId{ 
				GUID{ 0x98FE8B34, 0xF317, 0x459A, { 
					0x96, 0x27, 0x21, 0x12, 0x3E, 0xA9, 0x5B, 0xEA } } };

            // Start a remote operation
            winrt::AutomationRemoteOperation remoteOperation;
            const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
				remoteOperation.ImportConnectionBoundObject(
					m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
            const winrt::AutomationRemoteGuid extensionGuid = 
				remoteOperation.NewGuid(extensionId);
            const winrt::AutomationRemoteTextRange remoteTextRange = 
				remoteOperation.ImportTextRange(
					winrtTextRange.as<winrt::AutomationTextRange>());

            // The operands for the Math ML takes 3 parameters
            // 1. Text range over which the custom annotations need to be found.
            // 2. Math Format Type
            // 3. Output parameter that gives Math ML string
            std::vector<winrt::AutomationRemoteObject> extensionOperands;
            extensionOperands.emplace_back(remoteTextRange);
            extensionOperands.emplace_back(
				remoteOperation.NewInt(0 /*predefinedMathFormatType*/));
            extensionOperands.emplace_back(remoteOperation.NewEmpty());
            remoteConnectionBoundObject.CallExtension(
				extensionGuid, extensionOperands);

            const winrt::AutomationRemoteOperationResponseToken remoteMathStringToken = 
				remoteOperation.RequestResponse(extensionOperands[2]);
            const winrt::AutomationRemoteOperationResultSet results = 
				remoteOperation.Execute();
            winrt::check_hresult(results.OperationStatus());

            const winrt::hstring mathML = winrt::unbox_value<winrt::hstring>(
				results.GetResult(remoteMathStringToken));
            return mathML;
        }

winrt::AutomationTextRange ExpandToEnclosingSentenceUsingNonWrapperAPI(
	_In_ IUIAutomationElement* enclosingElement, 
	_In_ IUIAutomationTextRange* textRange)
{
    const winrt::com_ptr<IUIAutomationElement> winrtEnclosingElement = 
		MakeWinrtComPtr(enclosingElement);
    const winrt::com_ptr<IUIAutomationTextRange> winrtTextRange = MakeWinrtComPtr(textRange);

    // Guid: {98FE8B34-F317-459A-9627-21123EA95BEA} 
	// for expanding to enclosing unit sentence.
    static constexpr winrt::guid extensionId{ 
		GUID{ 0x98FE8B34, 0xF317, 0x459A, { 
			0x96, 0x27, 0x21, 0x12, 0x3E, 0xA9, 0x5B, 0xEA } } };

    winrt::CoreAutomationRemoteOperation remoteOperation;
    remoteOperation.ImportConnectionBoundObject(
		{ 1 }, m_connectionBoundObject.as<winrt::AutomationConnectionBoundObject>());
    remoteOperation.ImportTextRange(
		{ 3 }, winrtTextRange.as<winrt::AutomationTextRange>());

    const std::vector<uint8_t> bytecode =
    {
        // Version
        0x00, 0x00, 0x00, 0x00,

        // Instructions

        // NewGuid(2, extensionId)
        0x48, 0x00, 0x00, 0x00,
        0x02, 0x00, 0x00, 0x00,
        (extensionId.Data1 & 0xffu),
        ((extensionId.Data1 >> 8) & 0xffu),
        ((extensionId.Data1 >> 16) & 0xffu),
        ((extensionId.Data1 >> 24) & 0xffu),
        (extensionId.Data2 & 0xffu),
        ((extensionId.Data2 >> 8) & 0xffu),
        (extensionId.Data3 & 0xffu),
        ((extensionId.Data3 >> 8) & 0xffu),
        extensionId.Data4[0],
        extensionId.Data4[1],
        extensionId.Data4[2],
        extensionId.Data4[3],
        extensionId.Data4[4],
        extensionId.Data4[5],
        extensionId.Data4[6],
        extensionId.Data4[7],

        0x53, 0x00, 0x00, 0x00, // Instruction Id(CallExtension)
        0x01, 0x00, 0x00, 0x00, // Imported element on which CallExtension instruction needs to be executed
        0x02, 0x00, 0x00, 0x00, // GUID associated with custom pattern interface/method
        0x01, 0x00, 0x00, 0x00, // Count of the operands(parameters).
        0x03, 0x00, 0x00, 0x00, // parameter list. We have only 1 param here which is the imported text range(0x03)
    };

    // We need to get the modified or expanded range.
    remoteOperation.AddToResults({ 0x03 });

    // Execute remote operation to receive expanded range.
    winrt::AutomationRemoteOperationResult result = 
		remoteOperation.Execute(bytecode);
    VERIFY_ARE_EQUAL(
		winrt::AutomationRemoteOperationStatus::Success, result.Status());

    auto modifiedTextRange = 
		(result.GetOperand({ 0x03 })).as<winrt::AutomationTextRange>();

    return modifiedTextRange;
  }
};

void TestExtensions(
	_In_ IUIAutomationElement* enclosingElement, 
	_In_ IUIAutomationTextRange* range)
{
	// AT(like Narrator, NVDA, JAWS) is focused on Word document of version 
	// that supports the custom  patterns.
	// All modified ranges have same enclosing element  (in reality, we need
	// to get the enclosing element every time for the range we are working on).
	WordCustomPatternDataFetcher dataFetcher(enclosingElement);

	std::pair<winrt::AutomationTextRange, int> rangeMovedByPair = 
		dataFetcher.MoveBySentence(range, 2 /*moveBy*/);
	std::pair<winrt::AutomationTextRange, int> rangeMovedByEndpointPair = 
		dataFetcher.MoveEndpointBySentence(
			range, TextPatternRangeEndpoint_End, 2 /*moveBy*/);
	int pageNumber = 
		dataFetcher.GetCustomAttributeValue(
			range, AttributeIdentifier::PageNumber);
	winrt::hstring bookmarkName = dataFetcher.GetBookMarkName(range);
	winrt::AutomationTextRange expandedRange = 
		dataFetcher.ExpandToEnclosingSentence(range);
	winrt::hstring mathMLString = dataFetcher.GetMathMarkUp(range);
}
```

### Excel example

The next snippet shows a custom extension for Excel app that returns an array of cell names. This example demonstrates how an array of objects are usually returned when the CallExtension method is called for any provider (for example, Excel). For more details, see [Excel Custom Patterns](/office/uia/excel/excelcustompatterns).

The open-source wrapper libraries are essential for clients, as building bytecode manually is very difficult (especially when there are many operands or params in the remote operation). This example shows the raw form of ExpandToEnclosingUnit without using wrapper apis.

```cpp
namespace
{
    winrt::IInspectable GetISheetCellInventoryObject(
		_In_ IUIAutomationElement* excelElement)
    {
        winrt::com_ptr<IUIAutomationElement> winrtElement = 
			MakeWinrtComPtr(excelElement);

        // Guid: {654823FE-A483-4915-8709-67266866E518} 
		// to get ISheetCellInventory as a connection bound object.
        static constexpr winrt::guid extensionId{ 
			GUID{ 0x654823FE, 0xA483, 0x4915, { 
				0x87, 0x09, 0x67, 0x26, 0x68, 0x66, 0xE5, 0x18 } } };

        // Start a remote operation
        winrt::AutomationRemoteOperation remoteOperation;
        const winrt::AutomationRemoteElement remoteElement = 
			remoteOperation.ImportElement(winrtElement.as<winrt::AutomationElement>());
        const winrt::AutomationRemoteGuid extensionGuid = 
			remoteOperation.NewGuid(extensionId);

        std::vector<winrt::AutomationRemoteObject> extensionOperands;
        extensionOperands.emplace_back(remoteOperation.NewEmpty());

        remoteElement.CallExtension(
			extensionGuid, winrt::array_view(extensionOperands));
        const winrt::AutomationRemoteOperationResponseToken connectionBoundObjectToken = 
			remoteOperation.RequestResponse(extensionOperands[0]);

        const winrt::AutomationRemoteOperationResultSet results = 
			remoteOperation.Execute();
        winrt::check_hresult(results.OperationStatus());

        const winrt::IInspectable inspectable = 
			results.GetResult(connectionBoundObjectToken);
        return inspectable;
    }

    std::vector<winrt::hstring> GetCellsWithFormula(
		_In_ IUIAutomationElement* excelElement)
    {
        winrt::IInspectable connectionBoundISheetCellInventoryObj = 
			GetISheetCellInventoryObject(excelElement);

        // Guid: {24E137F2-4FFF-4F50-84AD-2ACD780E7E1F} 
		// for cells with formula in the excel sheet.
        static constexpr winrt::guid extensionId{ 
			GUID{ 0x24E137F2, 0x4FFF, 0x4F50, { 
				0x84, 0xAD, 0x2A, 0xCD, 0x78, 0x0E, 0x7E, 0x1F } } };

        // Start a remote operation.
        winrt::AutomationRemoteOperation remoteOperation;
        const winrt::AutomationRemoteConnectionBoundObject remoteConnectionBoundObject = 
			remoteOperation.ImportConnectionBoundObject(
				connectionBoundISheetCellInventoryObj.as<winrt::AutomationConnectionBoundObject>());
        const winrt::AutomationRemoteGuid extensionGuid = 
			remoteOperation.NewGuid(extensionId);

        // The operands for the custom method, specific to cells with a formula,
        // take 1 parameter and an Output parameter that holds the custom value 
		  // (which is an array of cell names).
        std::vector<winrt::AutomationRemoteObject> extensionOperands;
        extensionOperands.emplace_back(remoteOperation.NewEmpty());
        remoteConnectionBoundObject.CallExtension(extensionGuid, extensionOperands)

        const winrt::AutomationRemoteOperationResponseToken remoteCellNamesToken = 
			remoteOperation.RequestResponse(extensionOperands[0]);
        winrt::AutomationRemoteOperationResultSet results = 
			remoteOperation.Execute();

        winrt::check_hresult(results.OperationStatus());
        const winrt::IVector<winrt::IInspectable> inspectableArray = 
			(results.GetResult(remoteCellNamesToken)).as<winrt::IVector<winrt::IInspectable>>();

        std::vector<winrt::hstring> cellNames;
        for (const IInspectable& inspectable : inspectableArray)
        {
            cellNames.emplace_back(inspectable.as<winrt::hstring>());
        }

        return cellNames;
    }
}
```

## See also

- [UIA control pattern](uiauto-controlpatternsoverview.md)
- [Windows.UI.UIAutomation.Core Namespace](/uwp/api/windows.ui.uiautomation.core)
- [UI Automation Custom Extensions in Office](/office/uia/)
- [Windows UIAutomation platform utility libraries](https://github.com/microsoft/Microsoft-UI-UIAutomation)
- [Word Custom Patterns](/office/uia/word/wordcustompatterns)
- [Excel Custom Patterns](/office/uia/excel/excelcustompatterns)
