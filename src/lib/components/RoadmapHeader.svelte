<script lang="ts">
    let { title } = $props();
    let showDropdown = $state(false);
    let dropdownRef: HTMLElement | null = $state(null);
    let buttonRef: HTMLElement | null = $state(null);

    const roadmaps = [
        { name: 'Lớp 6 (Pre-GS6)', path: '/pre-gs6' },
        { name: 'Lớp 7 (Pre-GS7)', path: '/pre-gs7' },
        { name: 'Lớp 8 (Pre-GS8)', path: '/pre-gs8' },
        { name: 'Lớp 9 (Pre-GS9)', path: '/pre-gs9' }
    ];

    function toggleDropdown(event: MouseEvent) {
        event.stopPropagation();
        showDropdown = !showDropdown;
    }

    function handleClick(event: MouseEvent) {
        if (!dropdownRef?.contains(event.target as Node) && !buttonRef?.contains(event.target as Node)) {
            showDropdown = false;
        }
    }

    function handleRoadmapClick() {
        showDropdown = false;
    }

    // Add click listener when component mounts
    $effect(() => {
        document.addEventListener('click', handleClick);
        return () => {
            document.removeEventListener('click', handleClick);
        };
    });
</script>

<header class="mb-6">
    <div class="mb-3 text-center relative gap-3 flex flex-col sm:flex-row justify-between items-center">
        <div class="flex gap-2">
            <a href="/" class="home-button btn btn-primary py-1 px-3">Về trang chủ</a>
            <div class="dropdown dropdown-start">
                <button 
                    bind:this={buttonRef}
                    class="btn btn-primary py-1 px-3" 
                    onclick={toggleDropdown}
                >
                    Chọn lộ trình
                </button>
                {#if showDropdown}
                    <ul 
                        bind:this={dropdownRef}
                        class="dropdown-content z-[1] menu p-2 shadow-lg bg-base-100 rounded-box w-52 mt-4"
                    >
                        {#each roadmaps as roadmap (roadmap.path)}
                            <li>
                                <a 
                                    href={roadmap.path}
                                    class="text-base hover:bg-primary hover:text-primary-content"
                                    onclick={handleRoadmapClick}
                                >
                                    {roadmap.name}
                                </a>
                            </li>
                        {/each}
                    </ul>
                {/if}
            </div>
        </div>

        <div class="flex flex-col items-center">
            <h1 class="text-primary mb-2 text-2xl font-bold">
                {title}
            </h1>
        </div>
        <div></div>
    </div>
    <hr />
</header> 