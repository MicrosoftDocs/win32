---
title: Minimal DXCore application
description: The full source code listing for a minimal DXCore application.
ms.custom: 19H1
ms.topic: article
ms.date: 06/21/2019
---

# Minimal DXCore application

This topic presents the full source code listing for a minimal DXCore application (written in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis)). Most of the code shown below is explained in the topic [Using DXCore to enumerate adapters](dxcore-enum-adapters.md).

## Full source code listing of a minimal DXCore application

If you want to build and run this source code example then first, in Visual Studio, create a new **Windows Console Application (C++/WinRT)** project. Then edit `pch.h` and `main.cpp` to look like the listings below.

The code example below uses [C++/WinRT](/windows/uwp/cpp-and-winrt-apis). However, in order to keep the use of the APIs is transparent, it doesn't use the [winrt::com_ptr::capture function](/uwp/cpp-ref-for-winrt/com-ptr#com_ptrcapture-function).

```cppwinrt
// pch.h
#pragma once
#include <algorithm>
#include <functional>

#include <unknwn.h>
#include <winrt/base.h>
#include <initguid.h>
#include <dxcore.h>
```

```cppwinrt
// main.cpp
#include "pch.h"

//
// Example 1 : TryFindComputeAdapter
//
// Shows how to enumerate adapters of a specific type, and select one based on its properties.
//

winrt::com_ptr<IDXCoreAdapter> TryFindComputeAdapter()
{
    // You begin DXCore adapter enumeration by creating an adapter factory.
    winrt::com_ptr<IDXCoreAdapterFactory> adapterFactory;
    winrt::check_hresult(::DXCoreCreateAdapterFactory(adapterFactory.put()));

    // From the factory, retrieve a list of all the Direct3D 12 Core Compute adapters.
    winrt::com_ptr<IDXCoreAdapterList> d3D12CoreComputeAdapters;
    GUID attributes[]{ DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE };
    winrt::check_hresult(
        adapterFactory->CreateAdapterList(_countof(attributes),
            attributes,
            d3D12CoreComputeAdapters.put()));

    // If there are any hardware adapters, then choose the first.
    // Otherwise, choose the first sofware adapter.
    winrt::com_ptr<IDXCoreAdapter> preferredAdapter;

    const uint32_t count{ d3D12CoreComputeAdapters->GetAdapterCount() };

    for (uint32_t i = 0; i < count; ++i)
    {
        winrt::com_ptr<IDXCoreAdapter> candidateAdapter;
        winrt::check_hresult(
            d3D12CoreComputeAdapters->GetAdapter(i, candidateAdapter.put()));

        bool isHardware{ false };
        winrt::check_hresult(candidateAdapter->GetProperty(
            DXCoreAdapterProperty::IsHardware,
            &isHardware));

        if (isHardware)
        {
            // Choose the first hardware adapter, and stop looping.
            preferredAdapter = candidateAdapter;
            break;
        }

        // Otherwise, ensure that (as long as there are *any* adapters) we'll
        // at least choose one.
        if (!preferredAdapter)
        {
            preferredAdapter = candidateAdapter;
        }
    }

    return preferredAdapter;
}

//
// Example 2 : TryFindHardwareHighPerformanceGraphicsAdapter
//
// Shows how to select the preferred adapter by sorting an adapter list.
//

winrt::com_ptr<IDXCoreAdapter> TryFindHardwareHighPerformanceGraphicsAdapter()
{
    // You begin DXCore adapter enumeration by creating an adapter factory.
    winrt::com_ptr<IDXCoreAdapterFactory> adapterFactory;
    winrt::check_hresult(::DXCoreCreateAdapterFactory(adapterFactory.put()));

    // From the factory, retrieve a list of all the Direct3D 12 Graphics adapters.
    winrt::com_ptr<IDXCoreAdapterList> d3D12GraphicsAdapters;
    GUID attributes[]{ DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS };
    winrt::check_hresult(
        adapterFactory->CreateAdapterList(_countof(attributes),
            attributes,
            d3D12GraphicsAdapters.put()));

    DXCoreAdapterPreference sortPreferences[]{
        DXCoreAdapterPreference::Hardware, DXCoreAdapterPreference::HighPerformance };

    // Ask the OS to sort for the highest performance hardware adapter.
    winrt::check_hresult(d3D12GraphicsAdapters->Sort(_countof(sortPreferences), sortPreferences));

    winrt::com_ptr<IDXCoreAdapter> preferredAdapter;

    if (d3D12GraphicsAdapters->GetAdapterCount() > 0)
    {
        winrt::check_hresult(d3D12GraphicsAdapters->GetAdapter(0, preferredAdapter.put()));
    }

    return preferredAdapter;
}

//
// Example 3 : SetDesiredMemoryReservation
//
// Shows how to get and set properties on an adapter. In this case, we
// set the desired memory reservation (in bytes) for node 0's local segment group.
//

void SetDesiredMemoryReservation(winrt::com_ptr<IDXCoreAdapter> const& adapter, uint64_t reservation)
{
    DXCoreAdapterMemoryBudgetNodeSegmentGroup nodeSegmentGroup{};
    nodeSegmentGroup.nodeIndex = 0;
    nodeSegmentGroup.segmentGroup = DXCoreSegmentGroup::Local;

    DXCoreAdapterMemoryBudget memoryBudget{};
    winrt::check_hresult(adapter->QueryState(
        DXCoreAdapterState::AdapterMemoryBudget,
        &nodeSegmentGroup,
        &memoryBudget));

    // Clamp the reservation to what's available.
    reservation = std::min<uint64_t>(reservation, memoryBudget.availableForReservation);

    winrt::check_hresult(adapter->SetState(
        DXCoreAdapterState::AdapterMemoryBudget,
        &nodeSegmentGroup,
        &reservation));
}

//
// Example 4: WatchedAdapterList
//
// Shows how to register for, and handle, notifications; in this case, the
// notification that the adapter list has become stale.
//

class WatchedAdapterList
{
    winrt::com_ptr<IDXCoreAdapterList> m_adapters;
    std::function<void()> m_callback;

    uint32_t m_eventCookie = 0;

public:
    WatchedAdapterList() = default;

    ~WatchedAdapterList()
    {
        Close();
    }

    // Watches the given adapter list. When it goes stale, the callback is
    // called from an arbitrary thread.
    void Watch(
        winrt::com_ptr<IDXCoreAdapterList> adapters,
        std::function<void()> callback)
    {
        Close();

        m_adapters = adapters;
        m_callback = callback;
        m_adapters = std::move(adapters);
        m_callback = std::move(callback);

        winrt::com_ptr<IDXCoreAdapterFactory> factory;
        winrt::check_hresult(m_adapters->GetFactory(factory.put()));

        winrt::check_hresult(factory->RegisterEventNotification(
            m_adapters.get(),
            DXCoreNotificationType::AdapterListStale,
            OnAdapterListStale,
            this,
            &m_eventCookie));
    }

    void Close()
    {
        if (!m_adapters)
        {
            assert(m_eventCookie == 0);
            return;
        }

        winrt::com_ptr<IDXCoreAdapterFactory> factory;
        winrt::check_hresult(m_adapters->GetFactory(factory.put()));

        HRESULT hr = factory->UnregisterEventNotification(m_eventCookie);

        m_eventCookie = 0;
        m_callback = nullptr;
        m_adapters = nullptr;

        winrt::check_hresult(hr);
    }

    explicit operator bool() const
    {
        return static_cast<bool>(m_adapters);
    }

private:
    static void WINAPI OnAdapterListStale(
        DXCoreNotificationType notificationType,
        IUnknown* staleObject,
        void* context)
    {
        WatchedAdapterList* self = static_cast<WatchedAdapterList*>(context);
        if (self->m_callback)
            self->m_callback();
    }
};

static void AdapterListIsStaleCallback()
{
    // Respond to the `d3D12CoreComputeAdapters` adapter list becoming stale.
}

int main()
{
    winrt::init_apartment();

    // Example 1.
    winrt::com_ptr<IDXCoreAdapter> computeAdapter{ TryFindComputeAdapter() };

    // Example 2.
    winrt::com_ptr<IDXCoreAdapter> graphicsAdapter{ TryFindHardwareHighPerformanceGraphicsAdapter() };

    if (computeAdapter)
    {
        // Example 3.
        SetDesiredMemoryReservation(computeAdapter, 0x40000000);
    }

    winrt::com_ptr<IDXCoreAdapterFactory> adapterFactory;
    winrt::check_hresult(::DXCoreCreateAdapterFactory(adapterFactory.put()));
    winrt::com_ptr<IDXCoreAdapterList> d3D12CoreComputeAdapters;
    GUID attributes[]{ DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE };
    winrt::check_hresult(
        adapterFactory->CreateAdapterList(_countof(attributes),
            attributes,
            d3D12CoreComputeAdapters.put()));

    // Example 4.
    WatchedAdapterList watchedAdapterList;
    watchedAdapterList.Watch(d3D12CoreComputeAdapters, AdapterListIsStaleCallback);
}
```

## Related topics

* [Using DXCore to enumerate adapters](dxcore-enum-adapters.md)
* [DXCore Reference](./dxcore-reference.md)
* [Direct3D 12 graphics](../direct3d12/direct3d-12-graphics.md)
