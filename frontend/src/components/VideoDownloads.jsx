export default (linkprop) => {
    return (
        <>
            <section>
                <h1 className="pb-5">
                    downloads tips so aparece quando clicar kkk
                </h1>
                <div className="ratio ratio-16x9 container w-50">
                    <iframe src={linkprop.link} allowFullScreen></iframe>
                </div>
                <div className="pt-5">links tipe download</div>
            </section>
        </>
    );
};
