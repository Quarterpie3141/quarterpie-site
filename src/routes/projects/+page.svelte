<svelte:head>
	<title>Projects | Quarterpie</title>
</svelte:head>

<script lang="ts">
	type Project = {
		name: string;
		tag: string;
		description: string;
		status: string;
		year: string;
		link?: string;
	};

	const projects: Project[] = [
		{
			name: '???',
			tag: '—',
			description: 'Project index is currently being compiled. Check back soon.',
			status: 'In Progress',
			year: '2026'
		},
		{
			name: '???',
			tag: '—',
			description: 'Project index is currently being compiled. Check back soon.',
			status: 'In Progress',
			year: '2026'
		},
		{
			name: '???',
			tag: '—',
			description: 'Project index is currently being compiled. Check back soon.',
			status: 'In Progress',
			year: '2026'
		},
		{
			name: '???',
			tag: '—',
			description: 'Project index is currently being compiled. Check back soon.',
			status: 'In Progress',
			year: '2026'
		}
	];
</script>

<div class="flex flex-col md:flex-row justify-between">
	<div class="ml-8 mt-8 w-max text-white leading-tight">
		<h1 class="mb-0 text-4xl leading-tight">Quarterpie</h1>
		<div class="flex w-full justify-between mb-1.5">
			<h2 class="text-xl leading-none">PER AUS</h2>
			<h2 class="text-xl leading-none">/projects</h2>
		</div>
		<div class="flex w-full justify-between mb-1">
			<h2 class="text-xl leading-none">Quarterpie</h2>
			<h2 class="text-xl leading-none">Labs</h2>
		</div>
		<div class="flex w-full justify-between mb-1">
			<img class="w-12 h-12 my-auto" src="/branding/logo_white.png" alt="Quarterpie Labs Logo" />
			<div class="leading-none">
				<h5 class="text-md mb-0.5">creativity</h5>
				<h5 class="text-md mb-0.5">engineered</h5>
				<h5 class="text-md mb-0.5">8906.96050</h5>
			</div>
		</div>
		<h2 class="text-xl leading-none">EXT_Projects.Index</h2>
	</div>

	<div class="text-white ml-8 mr-8 md:ml-0 md:mr-8 mt-16 w-auto md:w-2/3 md:max-w-248 md:mt-8">
		<div class="h-1 bg-white mb-5"></div>
		<div class="flex justify-between items-end gap-4 mb-5">
			<div>
				<h2 class="text-xl leading-tight">Project</h2>
				<h2 class="text-4xl leading-none">Showcase</h2>
			</div>
			<p class="text-xs md:text-sm text-white/80">{projects.length} entries</p>
		</div>

		<div class="h-1 bg-white mb-5"></div>
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-5 pb-26 md:pb-22">
			{#each projects as project}
				<article class="border border-white p-4 md:p-5">
					<div class="flex justify-between items-start gap-4 mb-2">
						<div>
							<h3 class="text-lg md:text-xl leading-none mb-1">{project.name}</h3>
							<p class="text-xs md:text-sm text-white/80">{project.tag}</p>
						</div>
						<p class="text-xs md:text-sm">{project.year}</p>
					</div>
					<p class="text-sm md:text-base leading-snug mb-4">{project.description}</p>
					<div class="flex justify-between items-center border-t border-white pt-3">
						<p class="text-xs md:text-sm">Status: {project.status}</p>
						{#if project.link}
							<a class="text-xs md:text-sm underline underline-offset-2 hover:no-underline" href={project.link}
								>Open</a
							>
						{/if}
					</div>
				</article>
			{/each}
		</div>

		<div class="h-1 bg-white mt-1 mb-4"></div>
		<div class="flex flex-wrap gap-x-6 gap-y-2 text-sm md:text-base">
			<a class="underline underline-offset-2 hover:no-underline" href="/">Landing</a>
			<a class="underline underline-offset-2 hover:no-underline" href="/about">About</a>
		</div>
	</div>
</div>

<div class="absolute right-0 bottom-2 left-2 flex pr-2">
	<div class="mr-5 mt-auto">
		<img class="h-8 w-auto my-auto" src="/branding/barcode.svg" alt="PDF417 Barcode" />
	</div>
	<div class="relative flex-1 min-w-0">
		<div class="w-max">
			<div class="flex justify-between gap-4">
				<div>
					<h5 class="text-[0.5rem] mb-0.5 text-white leading-none">RAAVH74</h5>
					<h5 class="text-[0.5rem] mb-0.5 text-white leading-none">EXTENSOR)</h5>
				</div>
				<div class="mb-0.5">
					<h5 class="text-[0.5rem] mb-0.5 text-white leading-none text-right">IRUSCU</h5>
					<h5 class="text-[0.5rem] mb-0.5 text-white leading-none">DIGITORUIM</h5>
				</div>
			</div>
			<div class="absolute left-0 right-0 h-0 border-t border-dashed border-white"></div>
			<div class="mt-1">
				<img class="h-3 w-full" src="/branding/cir_rec.svg" alt="cirrec" />
			</div>
		</div>
	</div>
</div>
