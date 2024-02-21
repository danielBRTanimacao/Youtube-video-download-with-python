export default (link) => {
    const regexLink = "^(https?://)?(www.youtube.com|youtu.be)/.+$";
    const classBtnDisable = document.querySelector("button#btn-for-submit");
    if (link.match(regexLink)) {
        return link.match(regexLink)[0];
    }
    classBtnDisable.innerHTML = "Link invalido";
    classBtnDisable.classList.remove("btn-primary");
    classBtnDisable.classList.add("btn-danger");
    return false;
};
