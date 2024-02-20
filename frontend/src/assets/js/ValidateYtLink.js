export default (link) => {
    const regexLink =
        "http(?:s?)://(?:www.)?youtu(?:be.com/watch?v=|.be/)([w-_]*)(&(amp;)?‌​[w?‌​=]*)?";
    console.log(link == regexLink);
};
