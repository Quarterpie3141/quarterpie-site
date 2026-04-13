<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import '@fontsource/ibm-plex-mono';
	let { children } = $props();
</script>
<style>
	:global(body){
		font-family: 'IBM Plex Mono', monospace;
	}
</style>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
{@render children()}


